"""Define constants for the PV Butler Server component."""
CONF_PLANT_ID = "plant_id"

DEFAULT_PLANT_ID = "0"

DEFAULT_NAME = "PV Butler"

SERVER_URLS = [
    "http://server.pvbutler.com/",
    "https://server.growatt.com/",
    "https://server-us.growatt.com/",
    "http://server.smten.com/",
]

DEFAULT_URL = SERVER_URLS[0]

DOMAIN = "pv_butler_server"

PLATFORMS = ["sensor"]

LOGIN_INVALID_AUTH_CODE = "502"
