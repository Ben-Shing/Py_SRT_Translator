# Py_SRT_Translator
這是一個簡單 Python SRT 檔案翻譯工具。

使用 Google Translate API 將 SRT 檔案翻譯成不同的語言

## 英文版按此 English Version
https://github.com/Ben-Shing/Py_SRT_Translator/blob/main/README_EN.md

# 要求
此腳本使用`Python 3.12`編寫。

需求在“requirements.txt”中查看。

執行以下命令來安裝所需庫。
````python
pip install -r requirements.txt
````

# 用法
使用前請確保安裝好依賴項。

使用以下命令以查看幫助訊息。
````python
python Py_SRT_Translator.py -help
````
使用以下命令以查看語言代號。
````python
python Py_SRT_Translator.py --list-lang
````

### 參數
- `<input_file>` - （必要）要輸入的文件，建議將文件拖曳到終端。

- `<target_language>` - （必要）語言代號，使用 `python Py_SRT_Translator.py --list-lang` 查看所有可用的語言代號。

- `<output_file>` - （可選）指定輸出路徑和檔案名，預設輸出路徑為與輸入檔案路徑相同，預設命名為 `<target_language>.srt`。

---
### 用法 1
1. 雙擊直接運行。

2. 依照提示輸入。

3. 取得輸出檔案。
### 用法 2
1. 使用終端運行。
````python
python Py_SRT_Translator.py
````
2. 與用法 1 步驟 2 和 3 相同。
### 用法 3
1. 使用終端運行。
````python
python Py_SRT_Translator.py <輸入檔> <目標語言> <輸出檔>
````
2. 取得輸出檔案。


# 規劃
- 中文日誌記錄
- 同時處理多個SRT文件
- 一次翻譯成多種語言
- 來自不同平台的翻譯