import logging
import os
import re

from googletrans import Translator, LANGUAGES
from tqdm import tqdm

class GoogleTranslator():

    def __init__(self):
        pass

    def translate_srt_file(self, input_file, target_language, output_file=None):

        # 設定日誌記錄
        logger = logging.getLogger("TranslatorLogger")
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # 檢查輸入檔案是否存在
        if not os.path.isfile(input_file):
            logger.error(f"Input file '{input_file}' does not exist.")
            return

        # 檢查檔案副檔名是否為 SRT:
        if not input_file.endswith('.srt'):
            logger.error(f"Input file '{input_file}' is not an SRT file.")
            return
        logger.info(f"Selected SRT file: {input_file}")

        # 檢查目標語言是否為空
        if not target_language:
            logger.error("Target language must be specified.")
            return

        # 檢查目標語言是否有效
        if target_language not in LANGUAGES:
            logger.error(f"Target language '{target_language}' is not supported.")
            return
        logger.info(f"Target language: {LANGUAGES[target_language]}({target_language})")

        # 讀取輸入 SRT 檔案
        logger.info("Reading input SRT file...")
        try:
            with open(input_file, 'r', encoding='utf-8') as file:
                srt_content = file.read()
        except Exception as e:
            logger.error(f"Failed to read input file '{input_file}'. Exception: {e}")
            return

        logger.info(f"Processing SRT file...")
        # 移除尾部空行
        srt_content = srt_content.strip()

        # 將 SRT 內容分割成個別的字幕塊
        subtitle_blocks = re.split(r'\n\s*\n', srt_content)

        # 建立翻譯器物件
        translator = Translator()
        logger.info("Translating subtitles...")
        # 翻譯每個字幕塊到目標語言
        translated_blocks = []
        for block in tqdm(subtitle_blocks, desc="Translating subtitles...", unit="Sentence"):
            lines = block.strip().split('\n')
            subtitle_number = lines[0]
            time_code = lines[1]
            subtitle_text = ' '.join(lines[2:])
            try:
                translated_text = translator.translate(subtitle_text, dest=target_language).text
            except Exception as e:
                logger.error(f"Error translating block: {block}\nException: {e}")
                translated_text = subtitle_text  # 保留原文
            translated_blocks.append(f"{subtitle_number}\n{time_code}\n{translated_text}")

        # 如果沒有指定輸出檔案，使用預設名稱
        if not output_file:
            output_file = f"{target_language}.srt"

        # 如果輸出檔案不包含路徑，則使用與輸入檔案相同的路徑
        if not os.path.dirname(output_file):
            output_file = os.path.join(os.path.dirname(input_file), output_file)

        # 檢查輸出檔案是否已存在
        if os.path.exists(output_file):
            will_overwrite = ""
            while will_overwrite.lower() not in ["y", "n"]:
                will_overwrite = input("File already exists. Do you want to overwrite it? (y/n): ")
                if will_overwrite.lower() not in ["y", "n"]:
                    print("Invalid input. Please enter 'y' or 'n'.")
            if will_overwrite.lower() == "n":
                return

        # 將翻譯後的字幕塊寫入輸出檔案
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write('\n\n'.join(translated_blocks))
            logger.info(f"Translated SRT file saved to '{output_file}'")
        except Exception as e:
            logger.error(f"Failed to write output file '{output_file}'. Exception: {e}")

    def show_available_languages():
        print("Available languages:")
        for code, language in LANGUAGES.items():
            print(f"{code}: {language}")

if __name__ == "__main__":

    # 設定日誌記錄
    logger = logging.getLogger("MainLogger")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.warning(f"You are running module directly. Entering debug mode.")

    # 加載翻譯器
    translator = GoogleTranslator()

    # 要求輸入
    input_file = input("Enter the path to the input SRT file: ")
    target_language = input("Enter the target language code (e.g., 'en' for English, 'zh-tw' for Traditional Chinese): ")
    output_file = input("Enter the path to the output translated SRT file (leave blank for default): ")

    # 翻譯 SRT 檔案
    translator.translate_srt_file(input_file, target_language, output_file)