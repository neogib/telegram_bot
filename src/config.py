import re

# Max retry settings
MAX_RETRIES = 10
RETRY_DELAY = 30  # seconds

# Allowed senders (Telegram user IDs)
ALLOWED_SENDERS = [
    7234154402,
    6700023868,
    -1001810124798,
    -1002219016950,
    -1002010433653,
    -1002577921673,
    -1002480481360,
    -1002381042005,
    -1002090258125,
    -1002458825510,
    -1002049726578,
    -1001903316574,
    -1001960878284,
    -1002091821802,
    -1001824357363,
]
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
