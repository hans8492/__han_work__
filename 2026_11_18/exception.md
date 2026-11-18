# Python 例外處理（Exception Handling）：一步一步練習

這份教材會帶你從認識錯誤訊息開始，由淺入深學會 Python 的例外處理語法：`try...except`、`else`、`finally`、主動拋出例外 `raise`，到進階的自訂例外類別（Custom Exception）。請打開 VS Code 或終端機，跟著每個步驟實際執行範例看看結果。

---

## 前置觀念：語法錯誤（Syntax Error）與例外（Exception）

寫程式時常見的錯誤分為兩種，在學習例外處理之前，先分清楚它們的差別：

- **語法錯誤（`SyntaxError`）**：程式碼不符合 Python 的語法規則（例如忘記加冒號 `:`、括號沒有成對）。這種錯誤發生時，程式**連開始執行都沒辦法**，不能用 `try...except` 攔截，必須直接修正程式碼。
- **例外（Exception / 執行期錯誤 Runtime Error）**：程式碼的語法完全正確，但**執行到一半**才因為資料或環境問題（例如除以 `0`、把非數字文字轉成整數、讀取不存在的檔案）而中斷。**例外處理就是用來處理這種執行期錯誤的機制。**

```python
# 語法錯誤範例：if 後面少了冒號，程式無法開始執行
# if True
#     print("Hello")
# SyntaxError: expected ':'

# 例外（執行期錯誤）範例：語法完全正確，但執行到第 2 行會中斷
print("程式開始")
result = 10 / 0
print("程式結束")  # 這一行不會被執行到
```

執行輸出（Traceback 錯誤追蹤訊息）：

```text
程式開始
Traceback (most recent call last):
  File "demo.py", line 2, in <module>
    result = 10 / 0
             ~~~^~~
ZeroDivisionError: division by zero
```

### 如何快速看懂 Traceback？

1. **先看最後一行**：得知錯誤的**類型**（`ZeroDivisionError`）與**原因**（`division by zero`）。
2. **再往上看行號**：找出錯誤發生在哪一個檔案、第幾行（`line 2`）以及哪一段算式。

### 為什麼需要例外處理？

如果不處理例外，只要發生一次錯誤，整支程式就會立刻崩潰結束；透過例外處理，我們可以：
- 攔截錯誤，讓程式不會意外中斷。
- 顯示對使用者友善的中文提示，而不是一連串難以理解的紅色錯誤訊息。
- 確保檔案或連線等資源在發生錯誤後依然能安全關閉。

### 常見內建例外一覽表

| 例外類型 | 常見發生原因 | 範例 |
| :--- | :--- | :--- |
| `ZeroDivisionError` | 除數為 `0` | `10 / 0` |
| `ValueError` | 資料型別正確，但「內容值」不合法 | `int("abc")` |
| `TypeError` | 對不相容的資料型別進行運算或操作 | `"10" + 5` |
| `IndexError` | 存取 `list` / `tuple` 時索引超出範圍 | `[1, 2, 3][5]` |
| `KeyError` | 存取 `dict` 時使用了不存在的鍵（key） | `{"a": 1}["b"]` |
| `FileNotFoundError` | 嘗試開啟不存在的檔案 | `open("missing.txt")` |

---

## 第 1 步：最基本的 `try...except` —— 攔截錯誤、避免程式崩潰

最基礎的結構是由 `try` 與 `except` 兩個區塊組成：
- **`try:`** 裡面放「可能會出錯的程式碼」。
- **`except 例外類型:`** 裡面放「萬一真的發生該錯誤時，要執行的補救措施」。

```python
def split_bill(total, people):
    try:
        per_person = total / people
        print(f"每人應付：{per_person:.0f} 元")
    except ZeroDivisionError:
        print("錯誤：分攤人數不能為 0！")

split_bill(600, 3)
split_bill(600, 0)
print("結帳流程繼續進行...")
```

執行輸出：

```text
每人應付：200 元
錯誤：分攤人數不能為 0！
結帳流程繼續進行...
```

- 當 `people` 為 `0` 時，`total / people` 會拋出 `ZeroDivisionError`。
- Python 會**立刻跳出 `try` 區塊**，不再執行下一行的 `print(f"每人應付：...")`，改為執行 `except ZeroDivisionError:` 裡的程式。
- 處理完例外後，後面的 `print("結帳流程繼續進行...")` 依然會正常執行，整支程式沒有崩潰。

---

## 第 2 步：捕捉特定例外（多重 `except`）與取得錯誤訊息（`as e`）

同一段程式碼往往可能出現好幾種不同的錯誤。我們可以：
1. 串接多個 `except` 分別針對不同錯誤給予不同回應。
2. 用元組 `(錯誤A, 錯誤B)` 一次接住多種採用相同處理方式的例外。
3. 加上 `as e`，把例外物件存進變數 `e`，取得系統原本的詳細錯誤訊息。

### 1. 多重 `except` 與 `as e`

```python
def calc_unit_price(total_text, count_text):
    try:
        total = int(total_text)
        count = int(count_text)
        unit_price = total / count
        print(f"單價：{unit_price:.1f} 元")
    except ValueError as e:
        print(f"輸入格式錯誤，請輸入整數！（系統訊息：{e}）")
    except ZeroDivisionError:
        print("數量不能為 0，無法計算單價！")

calc_unit_price("500", "4")
calc_unit_price("五百", "4")
calc_unit_price("500", "0")
```

執行輸出：

```text
單價：125.0 元
輸入格式錯誤，請輸入整數！（系統訊息：invalid literal for int() with base 10: '五百'）
數量不能為 0，無法計算單價！
```

### 2. 用元組合併捕捉，並以 `Exception` 作為保底防線

```python
def get_item(data, index_text):
    try:
        index = int(index_text)
        print("取得項目：", data[index])
    except (ValueError, IndexError) as e:
        print(f"查詢失敗（輸入非整數或索引超出範圍）：{e}")
    except Exception as e:
        # 保底防線：攔截其他未預期的錯誤，並印出錯誤類型名稱
        print(f"發生未預期的錯誤 [{type(e).__name__}]：{e}")

items = ["蘋果", "香蕉", "橘子"]
get_item(items, "1")     # 正常
get_item(items, "abc")   # 觸發 ValueError
get_item(items, "10")    # 觸發 IndexError
get_item(None, "0")      # 觸發 TypeError，由最後的 Exception 接住
```

執行輸出：

```text
取得項目： 香蕉
查詢失敗（輸入非整數或索引超出範圍）：invalid literal for int() with base 10: 'abc'
查詢失敗（輸入非整數或索引超出範圍）：list index out of range
發生未預期的錯誤 [TypeError]：'NoneType' object is not subscriptable
```

> [!IMPORTANT]
> 1. **越具體的例外要寫在越上面**，通用的 `Exception` 必須放在最後面。如果把 `except Exception:` 放在第一個，所有錯誤都會被它接走，後面的 `except ValueError:` 永遠不會被執行。
> 2. **不要寫空的 `except:`**（沒有指定任何例外類型）。空的 `except:` 連使用者按 `Ctrl+C` 中斷程式（`KeyboardInterrupt`）或系統結束（`SystemExit`）都會一起吃掉，還會把原本該修復的 Bug 隱藏起來。

---

## 第 3 步：完整結構 `try...except...else...finally` —— 四大區塊各司其職

除了 `try` 和 `except` 之外，Python 還提供 `else` 與 `finally` 兩個選用區塊，讓程式邏輯分得更乾淨：

```text
try:
    # 1. 嘗試執行可能發生例外的程式碼（保持精簡）
except 錯誤類型:
    # 2. 「有發生例外」時才執行
else:
    # 3. 「沒有發生任何例外」時才執行
finally:
    # 4. 「不管有沒有發生例外」最後都一定會執行
```

實際範例與對照測試：

```python
def divide_numbers(a, b):
    print(f"--- 開始計算 {a} / {b} ---")
    try:
        result = a / b
    except ZeroDivisionError:
        print("[except] 失敗：除數不能為 0！")
    except TypeError:
        print("[except] 失敗：請傳入數字型別！")
    else:
        print(f"[else] 計算成功，結果為：{result}")
    finally:
        print("[finally] 清理資源並結束本次計算。\n")

divide_numbers(10, 2)
divide_numbers(10, 0)
```

執行輸出：

```text
--- 開始計算 10 / 2 ---
[else] 計算成功，結果為：5.0
[finally] 清理資源並結束本次計算。

--- 開始計算 10 / 0 ---
[except] 失敗：除數不能為 0！
[finally] 清理資源並結束本次計算。
```

> [!TIP]
> **為什麼要把成功後的程式寫在 `else`，而不是全部塞進 `try` 裡面？**
> 讓 `try` 區塊只包住「真正可能出錯的那幾行」，可以避免後續處理程式碼意外拋出的錯誤，不小心被前面的 `except` 攔截錯地方，讓除錯更明確。

`finally` 在實務上最常搭配檔案讀取、網路連線或資料庫連線，用來確保無論過程中是否發生錯誤，資源都能順利關閉（在檔案讀寫時，也可以配合 `with open(...) as f:` 自動達成同樣的關閉效果）。

---

## 第 4 步：實戰應用 —— 搭配 `while` 迴圈打造輸入防呆機制

初學者最實用的場景之一，就是處理使用者的 `input()` 輸入。把 `while True:` 搭配 `try...except...else`，就能讓程式在使用者輸入錯誤時自動提示並要求重填，直到格式正確才離開迴圈：

```python
def ask_int(prompt):
    while True:
        raw = input(prompt)
        try:
            number = int(raw)
        except ValueError:
            print("格式不正確，請輸入有效的整數！")
        else:
            return number  # 轉換成功，結束迴圈並回傳結果

# 執行測試範例
score = ask_int("請輸入分數：")
print(f"你輸入的分數是：{score}")
```

操作示範輸出（假設使用者依序輸入 `abc`、`85`）：

```text
請輸入分數：abc
格式不正確，請輸入有效的整數！
請輸入分數：85
你輸入的分數是：85
```

---

## 第 5 步：主動拋出例外（`raise`）—— 檢查商業邏輯與資料合理性

有時候資料對 Python 來說完全合法，不會自動報錯，但**違反了程式的商業邏輯**（例如成績為 `-10` 分或 `150` 分、年齡為 `-3` 歲）。

這時可以使用 `raise` 主動拋出例外，清楚通知呼叫者「這個資料不合法」：

```python
def set_score(score):
    # 在 Python 中 bool 是 int 的子類別（isinstance(True, int) 為 True），因此額外排除 bool
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("成績必須是數字（int 或 float）！")
    if score < 0 or score > 100:
        raise ValueError(f"成績 {score} 超出合理範圍（必須介於 0 到 100 之間）！")
    print(f"成績設定成功：{score} 分")

for test_value in [95, -5, "滿分"]:
    try:
        set_score(test_value)
    except (TypeError, ValueError) as e:
        print(f"設定失敗：{e}")
```

執行輸出：

```text
成績設定成功：95 分
設定失敗：成績 -5 超出合理範圍（必須介於 0 到 100 之間）！
設定失敗：成績必須是數字（int 或 float）！
```

- 在寫函式或模組給其他程式呼叫時，遇到錯誤參數用 `raise` 拋出例外，比單純用 `print("錯誤")` 更好，因為外部程式可以用 `try...except` 接住並決定如何補救。

---

## 第 6 步：進階技巧 —— 自訂例外類別（Custom Exception）與例外鏈

當專案越來越複雜（例如銀行交易、電商庫存系統），內建的 `ValueError` 有時不足以清楚表達業務上的錯誤含義。這時候我們可以建立自己的例外類別，也可以將捕捉到的例外重新整理後往外拋出。

### 1. 自訂例外類別（繼承 `Exception`）

只要建立一個繼承自 `Exception` 的類別，就能讓錯誤名稱更有語意，還能順便攜帶客製化屬性（例如當前餘額與提款金額）：

```python
class InsufficientBalanceError(Exception):
    """當帳戶餘額不足以完成提款時拋出的例外。"""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"餘額不足！目前餘額為 {balance} 元，無法提領 {amount} 元。"
        )

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("提款金額必須大於 0！")
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(1000, 1500)
except InsufficientBalanceError as e:
    print(f"交易失敗：{e}")
    print(f"還差 {e.amount - e.balance} 元才能提領。")
except ValueError as e:
    print(f"金額錯誤：{e}")
```

執行輸出：

```text
交易失敗：餘額不足！目前餘額為 1000 元，無法提領 1500 元。
還差 500 元才能提領。
```

### 2. 重新拋出例外（Re-raise）與保留原始原因（`raise ... from e`）

在實務開發中，有時在 `except` 區塊記錄完錯誤後，仍需要把例外往外傳給上層：

- **單獨寫 `raise`**：在 `except` 區塊裡做完紀錄（如寫入 log）後，不帶任何參數直接寫 `raise`，就會把原本的例外原封不動往外丟。
- **`raise 新例外 from 原始例外`**：把底層的技術性錯誤（如 `ValueError`）轉換為更有意義的自訂例外，同時用 `from e` 保留原本的錯誤原因（稱為例外鏈 Exception Chaining），方便日後追蹤根因。

```python
class ConfigError(Exception):
    """設定檔解析失敗時拋出的例外。"""

def load_port(port_text):
    try:
        return int(port_text)
    except ValueError as e:
        # 轉換為更具語意的 ConfigError，同時保留原始的 ValueError 原因
        raise ConfigError(f"無法解析連接埠設定：{port_text!r}") from e

try:
    load_port("abc")
except ConfigError as e:
    print("設定錯誤：", e)
    print("原始原因：", e.__cause__)
```

執行輸出：

```text
設定錯誤： 無法解析連接埠設定：'abc'
原始原因： invalid literal for int() with base 10: 'abc'
```

---

## 例外處理語法速查總表

| 語法 | 說明與執行時機 | 範例 |
| :--- | :--- | :--- |
| `try:` | 包住可能發生例外的程式碼 | `try: x = int(text)` |
| `except 錯誤型別:` | 捕捉指定類型的例外 | `except ValueError:` |
| `except (錯誤A, 錯誤B) as e:` | 同時捕捉多種例外，並以 `e` 取得錯誤物件 | `except (ValueError, KeyError) as e:` |
| `except Exception as e:` | 保底攔截一般執行期例外（應放在最後） | `except Exception as e:` |
| `else:` | `try` 完全沒有發生例外時才執行 | `else: print("成功")` |
| `finally:` | 無論是否發生例外，最後一定會執行 | `finally: print("結束")` |
| `raise 錯誤型別("訊息")` | 主動拋出例外（檢查邏輯或資料合法性） | `raise ValueError("不可為負數")` |
| `raise` | 在 `except` 內原封不動重新拋出當前例外 | `except ValueError: ...; raise` |
| `raise 新例外 from e` | 轉換成新例外並保留原始錯誤原因 | `raise ConfigError("...") from e` |
| `class MyError(Exception):` | 自訂專屬的例外類別 | `class OutOfStockError(Exception):` |

---

## 練習題

請先自己動手寫寫看，再對照下方提示檢查：

1. **列表索引安全讀取**
   有一個清單 `fruits = ["蘋果", "香蕉", "芒果"]`。請寫一個函式 `safe_get(items, index)`：
   - 正常時回傳對應位置的水果名稱。
   - 若 `index` 超出範圍，捕捉 `IndexError` 並回傳 `"找不到該項目"`。
   - 若 `index` 不是整數，捕捉 `TypeError` 並回傳 `"索引必須是整數"`。
2. **字典查詢與型別轉換**
   有一個商品價格字典 `prices = {"紅茶": "30", "綠茶": "35", "試喝品": "免費"}`。請寫一個函式 `calc_total(item, qty)`，從 `prices` 取得價格並轉成 `int` 後乘以 `qty` 印出總金額；請用多重 `except` 分別處理查無商品（`KeyError`）與價格無法轉為數字（`ValueError`）的情況。
3. **體溫檢查函式（`raise` + 完整結構）**
   寫一個函式 `check_temperature(temp)`：如果 `temp < 30` 或 `temp > 45`，就主動 `raise ValueError("體溫數值不合理")`。接著在外部使用 `try...except...else...finally` 呼叫這個函式，沒出錯時在 `else` 印出 `"體溫記錄完成"`，最後在 `finally` 印出 `"量測結束"`。
4. **自訂例外類別 `OutOfStockError`**
   建立一個繼承自 `Exception` 的 `OutOfStockError(stock, request_qty)` 類別，以及函式 `order_item(stock, qty)`。當訂購數量 `qty` 大於庫存 `stock` 時拋出 `OutOfStockError`，並在外部用 `except OutOfStockError as e:` 捕捉後，印出目前庫存以及還缺少幾個。

提示：

```python
# 第 1 題提示：在 try 中回傳 items[index]，再用兩個 except 分別處理 IndexError 與 TypeError
# 第 2 題提示：price = int(prices[item])，prices[item] 可能觸發 KeyError，int(...) 可能觸發 ValueError
# 第 3 題提示：在函式內先判斷 if temp < 30 or temp > 45: raise ValueError(...)
# 第 4 題提示：可參考第 6 步的 InsufficientBalanceError，把 balance / amount 改成 stock / request_qty
```

---

## 常見問題

- **為什麼不建議只寫 `except:`（不指定錯誤類型）？**
  空的 `except:` 會把所有錯誤（包含 `KeyboardInterrupt`、`SystemExit` 甚至自己打錯變數名稱造成的 `NameError`）全部靜靜吞掉，讓你誤以為程式沒問題，日後極難除錯。建議明確列出預期的例外類型，最多在最後加上 `except Exception as e:` 並把錯誤印出或記錄下來。
- **為什麼不應該把幾十行程式碼全部包進同一個大 `try` 區塊？**
  `try` 區塊越大，出錯時就越難判斷是哪一行引發了例外，也很容易誤捕非預期的錯誤。應盡量只把真正會拋出例外的那 1～3 行放進 `try`，把成功後的後續步驟放到 `else` 裡。
- **在 `try` 或 `except` 裡面執行了 `return`，`finally` 還會執行嗎？**
  **會！** `finally` 一定會在函式真正 `return` 離開之前先執行完畢（這也是它適合用來釋放資源的原因）。
- **什麼時候該用 `if` 先檢查，什麼時候該用 `try...except`？**
  簡單的範圍檢查（如年齡不可小於 `0`）通常用 `if` 判斷即可；但像檔案開啟、網路請求、或把使用者輸入轉成數字（`int(raw)`）這類在檢查與執行之間容易出錯或不好預先判斷全部格式的動作，使用 `try...except` 會更簡潔安全。

---

## 完成檢查

- [ ] 能分辨語法錯誤（`SyntaxError`）與執行期例外（`Exception`），並看懂 Traceback 訊息。
- [ ] 能使用 `try...except` 攔截特定錯誤，避免程式直接崩潰。
- [ ] 能撰寫多重 `except`、合併元組捕捉，並使用 `as e` 取得錯誤訊息。
- [ ] 清楚 `try`、`except`、`else`、`finally` 四個區塊各自的執行時機。
- [ ] 能使用 `while True` 搭配 `try...except...else` 實作輸入防呆。
- [ ] 能使用 `raise` 主動拋出例外來檢查商業邏輯，並建立繼承 `Exception` 的自訂例外類別。
