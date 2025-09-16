import re

# Max retry settings
MAX_RETRIES = 10
RETRY_DELAY = 30  # seconds

# Allowed senders (Telegram user IDs)
ALLOWED_SENDERS = [
    7234154402,
    6700023868,
    -1002458825510,
]
ALLOWED_USER = 7234154402

RECIPIENT_ID = 7181780057

# Regex pattern to match messages ending with 'pump' or 'moon'
PATTERNS = [
    re.compile(
        r"([a-zA-Z0-9]*?(?=[a-zA-Z0-9]*[A-Z])(?=[a-zA-Z0-9]*[a-z])(?=[a-zA-Z0-9]*[0-9])[a-zA-Z0-9]+(pump|moon))\b"
    ),
    re.compile(r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])([a-zA-Z0-9]+(pump|moon))\b"),
    re.compile(
        r"([a-zA-Z0-9]*?(?=[a-zA-Z0-9]*[A-Z])(?=[a-zA-Z0-9]*[a-z])(?=[a-zA-Z0-9]*[0-9])[a-zA-Z0-9]+(pump|moon))"
    ),
]
