import os
import re


_TRUE_VALUES = {"true", "yes", "1", "enable", "y"}
_FALSE_VALUES = {"false", "no", "0", "disable", "n"}


def env(name: str, default: str = "") -> str:
    """Read a value exclusively from the process environment."""
    return os.getenv(name, default).strip()


def env_bool(name: str, default: bool = False) -> bool:
    value = env(name).lower()
    if value in _TRUE_VALUES:
        return True
    if value in _FALSE_VALUES:
        return False
    return default


def env_int(name: str, default=None):
    value = env(name)
    if not value:
        return default
    return int(value)


def env_list(name: str):
    return [item for item in env(name).split() if item]


def env_int_list(name: str):
    return [int(item) for item in env_list(name)]


# All application-specific values must be supplied through .env.
SESSION = env("SESSION")
API_ID = env_int("API_ID")
API_HASH = env("API_HASH")
BOT_TOKEN = env("BOT_TOKEN")

USE_CAPTION_FILTER = env_bool("USE_CAPTION_FILTER")
INDEX_CAPTION = env_bool("INDEX_CAPTION")
COVER = env_bool("COVER")
PICS = env_list("PICS")
MELCOW_PHOTO = env("MELCOW_PHOTO")
ADMINS = env_int_list("ADMINS")
CHANNELS = env_list("CHANNELS")
LOG_CHANNEL = env_int("LOG_CHANNEL")
BIN_CHANNEL = env_int("BIN_CHANNEL")
PREMIUM_LOGS = env_int("PREMIUM_LOGS")
DELETE_CHANNELS = env_list("DELETE_CHANNELS")
AUTH_CHANNELS = env_int_list("AUTH_CHANNELS")
AUTH_REQ_CHANNELS = env_int_list("AUTH_REQ_CHANNELS")
REQST_CHANNEL = env_int("REQST_CHANNEL")
SUPPORT_CHAT_ID = env_int("SUPPORT_CHAT_ID")

OWNER = env_int("OWNER")
CHANNEL_LINK = env("CHANNEL_LINK")
GROUP_LINK = env("GROUP_LINK")

DATABASE_URI = env("DATABASE_URI")
DATABASE_NAME = env("DATABASE_NAME")
COLLECTION_NAME = env("COLLECTION_NAME")
MULTIPLE_DB = env_bool("MULTIPLE_DB")
DATABASE_URI2 = env("DATABASE_URI2")

UPDATE_NOTIFICATION = env_bool("UPDATE_NOTIFICATION")
UPDATE_CHANNEL = env_int("UPDATE_CHANNEL")
IMAGE_FETCH = env_bool("IMAGE_FETCH")
LINK_PREVIEW = env_bool("LINK_PREVIEW")
ABOVE_PREVIEW = env_bool("ABOVE_PREVIEW")
TMDB_API_KEY = env("TMDB_API_KEY")
TMDB_POSTER = env_bool("TMDB_POSTER")
LANDSCAPE_POSTER = env_bool("LANDSCAPE_POSTER")

IS_VERIFY = env_bool("IS_VERIFY")
LOG_API_CHANNEL = env_int("LOG_API_CHANNEL")
VERIFY_IMG = env("VERIFY_IMG")
TUTORIAL = env("TUTORIAL")
TUTORIAL_2 = env("TUTORIAL_2")
TUTORIAL_3 = env("TUTORIAL_3")
SHORTENER_API = env("SHORTENER_API")
SHORTENER_WEBSITE = env("SHORTENER_WEBSITE")
SHORTENER_API2 = env("SHORTENER_API2")
SHORTENER_WEBSITE2 = env("SHORTENER_WEBSITE2")
SHORTENER_API3 = env("SHORTENER_API3")
SHORTENER_WEBSITE3 = env("SHORTENER_WEBSITE3")
TWO_VERIFY_GAP = env_int("TWO_VERIFY_GAP")
THREE_VERIFY_GAP = env_int("THREE_VERIFY_GAP")

FAST_MODE = env_bool("FAST_MODE")
MAX_BTN = env_bool("MAX_BTN")
MAX_BTNS = env_int("MAX_BTNS")
MSG_ALRT = env("MSG_ALRT")
DELETE_TIME = env_int("DELETE_TIME")
FILE_CAPTION = env("FILE_CAPTION")
IMDB_TEMPLATE = env("IMDB_TEMPLATE")
MAX_LIST_ELM = env_int("MAX_LIST_ELM")
NO_RESULTS_MSG = env_bool("NO_RESULTS_MSG")
P_TTI_SHOW_OFF = env_bool("P_TTI_SHOW_OFF")
IMDB = env_bool("IMDB")
TMDB_ON_SEARCH = env_bool("TMDB_ON_SEARCH")
AUTO_FILTER = env_bool("AUTO_FILTER")
AUTO_DELETE = env_bool("AUTO_DELETE")
LONG_IMDB_DESCRIPTION = env_bool("LONG_IMDB_DESCRIPTION")
SPELL_CHECK_REPLY = env_bool("SPELL_CHECK_REPLY")
MELCOW_NEW_USERS = env_bool("MELCOW_NEW_USERS")
PROTECT_CONTENT = env_bool("PROTECT_CONTENT")
PM_SEARCH = env_bool("PM_SEARCH")
EMOJI_MODE = env_bool("EMOJI_MODE")
BUTTON_MODE = env_bool("BUTTON_MODE")
STREAM_MODE = env_bool("STREAM_MODE")
PREMIUM_STREAM_MODE = env_bool("PREMIUM_STREAM_MODE")
MAINTENANCE = env_bool("MAINTENANCE")

# These values are also configurable; no built-in application data is retained.
LANGUAGES = {}
QUALITIES = env_list("QUALITIES")
SEASONS = env_list("SEASONS")
REACTIONS = env_list("REACTIONS")
STAR_PREMIUM_PLANS = {}
BAD_WORDS = set(env_list("BAD_WORDS"))

IS_FILE_LIMIT = env_bool("IS_FILE_LIMIT")
FILES_LIMIT = env_int("FILES_LIMIT")
QUALITY_LIMIT = env_bool("QUALITY_LIMIT")
FREE_QUALITIES = env_list("FREE_QUALITIES")

PORT = env_int("PORT")
NO_PORT = env_bool("NO_PORT")
ON_HEROKU = bool(env("DYNO"))
APP_NAME = env("APP_NAME")
BIND_ADRESS = env("WEB_SERVER_BIND_ADDRESS")
FQDN = env("FQDN")
SLEEP_THRESHOLD = env_int("SLEEP_THRESHOLD")
MULTI_CLIENT = env_bool("MULTI_CLIENT")
PING_INTERVAL = env_int("PING_INTERVAL")
HAS_SSL = env_bool("HAS_SSL")

if MULTIPLE_DB:
    DATABASE_URI2 = DATABASE_URI2
else:
    DATABASE_URI2 = DATABASE_URI

if HAS_SSL:
    URL = f"https://{FQDN}/" if FQDN else ""
else:
    URL = f"http://{FQDN}/" if FQDN else ""
