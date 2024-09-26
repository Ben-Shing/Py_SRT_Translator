import json
import logging
import os

from modules.handlers.arg import ArgHandler
from modules.translators.google import GoogleTranslator

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')
LANGS_PATH_PART = os.path.join(os.path.dirname(__file__), 'langs')
DEFAULT_CONFIG = {"language": "en"}

def load_config(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def create_config(file_path,content):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(content, file, indent=4)
    
def load_langs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

if __name__ == "__main__":

    # 設定日誌記錄
    logger = logging.getLogger("MainLogger")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 加載設定
    try:
        config = load_config(CONFIG_PATH)
        lang_config = config.get('language')
    except Exception as e:
        logger.error(f"Failed to load config file in '{CONFIG_PATH}'. Creating new config file.")
        logger.debug(f"Exception: {e}")
        create_config(CONFIG_PATH, DEFAULT_CONFIG)
        exit()

    # 加載語言檔
    if not lang_config:
        lang_config = "en"
    try:
        langs_path = os.path.join(LANGS_PATH_PART, lang_config + ".json")
        lang = load_langs(langs_path)
    except Exception as e:
        logger.error(f"Failed to load language file in '{langs_path}'. Exiting...")
        logger.debug(f"Exception: {e}")
        exit()

    # 加載翻譯器
    translator = GoogleTranslator()

    # 加載命令列參數
    arg_handler = ArgHandler()
    arg_handler.start(lang, translator)