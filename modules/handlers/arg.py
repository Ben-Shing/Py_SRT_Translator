import argparse


from modules.translators.google import GoogleTranslator

class ArgHandler():

    def __init__(self):
        pass

    def start(self, lang, translator: GoogleTranslator):
        # 添加命令列參數
        parser = argparse.ArgumentParser(description=lang["arg_description"])
        parser.add_argument('input_file', nargs='?', help=lang["arg_help_input_file"])
        parser.add_argument('target_language', nargs='?', help=lang["arg_help_target_language"])
        parser.add_argument('output_file', nargs='?', help=lang["arg_help_output_file"])
        parser.add_argument('--list-lang', action='store_true', help=lang["arg_help_list_lang"])

        args = parser.parse_args()

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