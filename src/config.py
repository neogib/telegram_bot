import re

# Max retry settings
MAX_RETRIES = 10
RETRY_DELAY = 30  # seconds

# Allowed senders (Telegram user IDs)
ALLOWED_SENDERS = [
    -1002480481360,
    7234154402,
    6700023868,
    -1002049726578,
    -1002090258125,
    -1002381042005,
    -1002045925410,
    -1002091821802,
    -1002219016950,
    -1002010433653,
    -1001960878284,
    -1001824357363,
    -1001903316574,
    -1001810124798,
    -1002135851444,
    -1001895548612,
]
RECIPIENT_ID = 7181780057

# Regex pattern to match messages ending with 'pump' or 'moon'
PATTERN = re.compile("([a-zA-Z0-9]+(pump|moon))")
