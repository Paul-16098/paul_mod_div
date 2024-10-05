import json
from pathlib import Path
import locale
import os


""" PATHS """
DIR_ROOT = Path(__file__).parent.parent

DIR_DATA_ROOT = DIR_ROOT / "data"
DIR_CONFIGS_ROOT = DIR_ROOT / "configs"
DIR_MODS_ROOT = DIR_ROOT / "mods"
DIR_RESULTS_ROOT = DIR_ROOT / "results"
DIR_TEMP_ROOT = DIR_DATA_ROOT / "tmp"
DIR_SOURCE_REPO = DIR_ROOT / "degrees-of-lewdity-master"
DIR_MODLOADER_ROOT = DIR_ROOT / "modloader"
DIR_MODLOADER_MODS = DIR_MODLOADER_ROOT / "mods"

os.makedirs(DIR_DATA_ROOT, exist_ok=True)
os.makedirs(DIR_CONFIGS_ROOT, exist_ok=True)
os.makedirs(DIR_MODS_ROOT, exist_ok=True)
os.makedirs(DIR_RESULTS_ROOT, exist_ok=True)
os.makedirs(DIR_TEMP_ROOT, exist_ok=True)

""" LANGS """
DIR_LANGS_ROOT = DIR_DATA_ROOT / "langs"
SYS_LANG = (locale.getdefaultlocale()[0]).lower()  # type: ignore # zh_cn
LANG_FILE = DIR_LANGS_ROOT / f"{SYS_LANG}.json"
LANG_FILE = LANG_FILE if LANG_FILE.exists() else DIR_LANGS_ROOT / "en_us.json"
with open(LANG_FILE, "r", encoding="utf-8") as fp:
    LANGS = json.load(fp)
with open(DIR_LANGS_ROOT / "en_us.json", "r", encoding="utf-8") as fp:
    DEFAULT_LANGS = json.load(fp)

""" SERVERS """
HOST = "localhost"
PORT = 52525

__all__ = [
    "DIR_ROOT",
    "DIR_SOURCE_REPO",
    "DIR_MODS_ROOT",
    "DIR_RESULTS_ROOT",
    "DIR_TEMP_ROOT",
    "DIR_DATA_ROOT",
    "DIR_CONFIGS_ROOT",
    "DIR_LANGS_ROOT",
    "DIR_MODLOADER_ROOT",
    "DIR_MODLOADER_MODS",

    "LANGS",
    "DEFAULT_LANGS",

    "HOST",
    "PORT",
]
