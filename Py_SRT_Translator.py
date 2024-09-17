import argparse
import json
import logging
import os

from googletrans import LANGUAGES

from Translators.Google import GoogleTranslator

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

def arg_handler():
    # 添加命令列參數
    parser = argparse.ArgumentParser(description="Translate SRT subtitle files to a specified language.")
    parser.add_argument('input_file', nargs='?', help="Path to the input SRT file.")
    parser.add_argument('target_language', nargs='?', help="Target language code (e.g., 'en' for English, 'zh-tw' for Traditional Chinese).")
    parser.add_argument('output_file', nargs='?', help="Path to the output translated SRT file. If not specified, the output file will be named as '<input_file>_<target_language>.srt'.")
    parser.add_argument('--list-lang', action='store_true', help="Show all available languages and their codes.")
    
    args = parser.parse_args()

    # 加載翻譯器
    translator = GoogleTranslator()
    
    # 處理命令列參數
    if args.list_lang:
        translator.show_available_languages()
    else:
        if not args.input_file and not args.target_language:
            input_file = input(lang["input_file"])
            target_language = input(lang["target_language"])
            output_file = input(lang["output_file"])
        elif not args.input_file or not args.target_language:
            parser.print_help()
            return
        else:
           input_file, target_language,output_file = args.input_file, args.target_language, args.output_file

        translator.translate_srt_file(input_file, target_language, output_file)

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

    arg_handler()