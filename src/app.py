import logging
import time
from pathlib import Path
from typing import cast

from dotenv import dotenv_values
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from telethon import TelegramClient, events

from .config import ALLOWED_SENDERS, MAX_RETRIES, PATTERN, RECIPIENT_ID, RETRY_DELAY

console = Console()


# Set up logging to help with debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="telegram_bot.log",
)
logger = logging.getLogger(__name__)


def get_env_path():
    current_file = Path(__file__)
    project_root = current_file.parent.parent
    env_path = project_root / ".env"
    return env_path


async def handle_message(event):
    """Handle incoming messages"""
    try:
        # Get the message text
        message_text = event.message.raw_text.strip()

        if "pump" not in message_text and "moon" not in message_text:
            logger.info(
                f"Message does not contain 'pump' or 'moon', chat_id: {event.chat_id}"
            )
            console.print(
                f"{time.asctime()} [bold red]❌ Message does not contain 'pump' or 'moon'[/bold red]. Message from {event.chat_id}"
            )
            return

        match = PATTERN.search(message_text)
        if not match:
            logger.info(f"Message does not match the pattern, chat_id: {event.chat_id}")
            console.print(
                f"{time.asctime()} [bold red]❌ Message does not match the pattern 'pump' or 'moon'[/bold red]. Message from {event.chat_id}"
            )
            return

        identifier = match.group()
        logger.info(f"Matched identifier: {identifier}")

        await event.client.send_message(RECIPIENT_ID, identifier)
        logger.info("Message sent to recipient")
        console.print(
            f"[bold green]✅ Message sent to recipient: [/bold green] {identifier}"
        )
        # await bot_communication(event.client, identifier)

    except Exception as e:
        logger.error(f"Error handling message: {e}")


def register_handlers(client):
    """Register all event handlers"""
    client.add_event_handler(
        handle_message, events.NewMessage(chats=ALLOWED_SENDERS, incoming=True)
    )


async def main():
    """Main function that sets up the client and handlers"""
    retry_count = 0
    env_path = get_env_path()
    api_id = int(cast(str, dotenv_values(env_path)["API_ID"]))
    api_hash = cast(str, dotenv_values(env_path)["API_HASH"])

    while retry_count < MAX_RETRIES:
        try:
            # Create the client with a session name
            async with TelegramClient("persistent_session", api_id, api_hash) as client:
                # async for dialog in client.iter_dialogs():
                #     print(f"Dialog: {dialog.name} ({dialog.id})")

                register_handlers(client)

                # successful connection
                logger.info("Client started successfully")
                success_text = Text("✅ Bot started successfully!")
                success_text.stylize("bold green")
                console.print(Panel(success_text, title="Status"))

                # Run until disconnected, but handle reconnection
                await client.run_until_disconnected()

        except Exception as e:
            retry_count += 1
            logger.error(f"Connection error (attempt {retry_count}/{MAX_RETRIES}): {e}")
            console.print(
                f"""[bold red]❌ Error occurred:[/bold red] Could not connect to server.
                Retrying... (attempt {retry_count}/{MAX_RETRIES})"""
            )

            if retry_count < MAX_RETRIES:
                logger.info(f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                logger.critical("Maximum retries reached. Exiting.")
                break
        finally:
            # Ensure client is disconnected before retrying
            if "client" in locals() and client.is_connected():
                await client.disconnect()
                logger.info("Client disconnected")
