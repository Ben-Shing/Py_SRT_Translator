# Py_SRT_Translator
This is a simple Python SRT file translator.

Translating SRT files into different languages using Google Translate API

## 中文版按此 Chinese Version
https://github.com/Ben-Shing/Py_SRT_Translator/blob/main/README.md

# Requirements
This script is written in `Python 3.12`.

Module requirements is written in `requirements.txt`.

To install, run the following command.
```python
pip install -r requirements.txt
```

# Usage
Make sure to install the dependencies before using.

Type the following command to see the help message.
```python
python Py_SRT_Translator.py -help
```
Type the following command to see the language code.
```python
python Py_SRT_Translator.py --list-lang
```

### Parameters
- `<input_file>` - (Required) File to be input, recommend dragging the file to the terminal.

- `<target_language>` - (Required) Language Code, using `python Py_SRT_Translator.py --list-lang` to see all available language code.

- `<output_file>` - (Optional) Specified the output location and file name, output file will be saved at the same location with the input file and named `<target_language>.srt` by default.

---
### Usage 1
1. Run the script directly by double-clicking.
2. Follow the instructions to input.
3. Get the output file.
### Usage 2
1. Run the script using terminal.
```python
python Py_SRT_Translator.py
```
2. Same with Usage 1 step 2 and 3.
### Usage 3
1. Run the script using terminal.
```python
python Py_SRT_Translator.py <input_file> <target_language> <output_file>
```
2. Get the output file.


# Plannings
- Chinese logging
- Multiple SRT files handling
- Translate into multiple languages at once
- Translators from different platforms