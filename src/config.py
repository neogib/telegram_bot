import re

# Max retry settings
MAX_RETRIES = 10
RETRY_DELAY = 30  # seconds

# Allowed senders (Telegram user IDs)
ALLOWED_SENDERS = [
    -1002480481360,
    7234154402,
    6700023868,
]
RECIPIENT_ID = 6700023868

# Regex pattern to match messages ending with 'pump' or 'moon'
PATTERN = re.compile("([a-zA-Z0-9]+(pump|moon))")
