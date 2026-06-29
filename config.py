import os

API_ID = int(os.getenv("API_ID", "29568441"))
API_HASH = os.getenv("API_HASH", "b32ec0fb66d22da6f77d355fbace4f2a")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_STRING = os.getenv("ASSISTANT_SESSION")
MAIN_OWNER = int(os.getenv("OWNER_ID", "8673494392"))
DEPLOYED_OWNER_ID = int(os.getenv("OWNER_ID", "8673494392"))
SEARCH_API_URL = os.getenv("SEARCH_API_URL", "https://search-api.kustbotsweb.workers.dev")
CURRENT_DYNO = os.getenv("DYNO_ID", os.getenv("DYNO", f"Worker-{os.getpid()}"))
MAX_BOTS_PER_DYNO = 20
RATE_LIMIT_COUNT = 4
RATE_LIMIT_WINDOW = 6
MAX_TITLE_LEN = 30
PORT = int(os.getenv("PORT", "8080"))
COOKIES_FILE = os.getenv("COOKIES_FILE", "cookies.txt")
