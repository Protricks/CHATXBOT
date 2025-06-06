from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "6435225"
# -------------------------------------------------------------
API_HASH = "4e984ea35f854762dcde906dce426c2d"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7103710760:AAF0wDqkEWMG5H6d9Tkulcm-RQyVb-t2UEA")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = int(getenv("OWNER_ID", "6035523795"))
SUPPORT_GRP = "Nxt_Bots"
UPDATE_CHNL = "Nxt_Bots"
OWNER_USERNAME = "Mafia_xDD"
