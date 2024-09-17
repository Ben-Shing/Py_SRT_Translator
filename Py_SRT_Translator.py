import argparse
# import logging

from googletrans import LANGUAGES

from Translators.Google import GoogleTranslator

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
            input_file = input("Enter the path to the input SRT file: ")
            target_language = input("Enter the target language code (e.g., 'en' for English, 'zh-tw' for Traditional Chinese): ")
            output_file = input("Enter the path to the output translated SRT file (leave blank for default): ")
        elif not args.input_file or not args.target_language:
            parser.print_help()
            return
        else:
           input_file, target_language,output_file = args.input_file, args.target_language, args.output_file

        translator.translate_srt_file(input_file, target_language, output_file)

if __name__ == "__main__":

    arg_handler()