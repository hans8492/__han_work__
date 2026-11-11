# Python 檔案讀取練習

這份練習會帶你使用 Python 讀取文字檔。請先確認資料夾中有以下兩個檔案：

```text
2026_11_11/
  read_file_example.py
  sample_data.txt
```

## 第 1 步：執行範例程式

在 VS Code 開啟 `2026_11_11` 資料夾，開啟終端機並執行：

```powershell
python read_file_example.py
```

程式會依序示範幾種讀取方式。`sample_data.txt` 是程式要讀取的範例檔，請先不要更改檔名。

## 第 2 步：認識 open()

讀取檔案時，常見寫法如下：

```python
file = open("sample_data.txt", "r", encoding="utf-8")
```

- `open()` 用來開啟檔案。
- `sample_data.txt` 是檔案名稱。這種寫法會從目前的工作資料夾尋找它。
- `"r"` 代表以讀取模式開啟檔案（read）。
- `encoding="utf-8"` 用來正確讀取包含中文的文字。

## 第 3 步：使用 with 讀取全文

實際寫程式時，建議使用 `with`。離開縮排區塊後，Python 會自動關閉檔案。

```python
with open("sample_data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

`read()` 會一次讀取整個檔案，結果是字串。請在 `read_file_example.py` 找到「read() 讀取全文」區段，試著在讀取內容前加上 `print(type(content))`，確認它的資料型態。

## 第 4 步：讀取一行

```python
with open("sample_data.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    print(first_line)
```

`readline()` 每次讀取一行。請試著多寫一行 `print(file.readline())`，觀察第二次讀到哪一行。

## 第 5 步：逐行處理

檔案較大時，可以一次處理一行，不必把全文都存進記憶體：

```python
with open("sample_data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip("\n"))
```

每一行通常會包含換行字元 `\n`。`rstrip("\n")` 會移除行尾的換行字元，避免輸出時多出空白行。

## 第 6 步：讀成清單並計算行數

```python
with open("sample_data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
print(f"總共有 {len(lines)} 行")
```

`readlines()` 會把每一行放進一個清單（list），因此可以用 `len()` 計算行數。清單中的每個字串通常也會保留行尾的 `\n`。

## 動手練習

1. 在 `sample_data.txt` 最後新增一行自己的文字，再執行程式，確認新內容有被讀到。
2. 使用 `readlines()` 讀取內容，印出第 1 行（清單索引從 `0` 開始）。
3. 把逐行輸出的程式改成印出「行號：內容」，例如 `1: Python 檔案讀取練習`。
4. 修改範例檔的內容，重新計算總行數，確認結果會跟著改變。

## 常見問題

- **找不到檔案（FileNotFoundError）**：確認終端機目前位於 `2026_11_11` 資料夾，並檢查檔名是否為 `sample_data.txt`。
- **中文顯示錯誤**：確認 `open()` 中有設定 `encoding="utf-8"`。
- **程式已經讀不到內容**：讀取位置會往檔案尾端移動。若要重新讀取，請重新開啟檔案，或在檔案開啟時使用 `file.seek(0)` 回到開頭。