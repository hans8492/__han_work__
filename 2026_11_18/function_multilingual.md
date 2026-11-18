# Python 函式呼叫與引數指南 / Python Function Call & Argument Guide / Python 関数呼び出しと引数ガイド

本說明檔根據 [`function.ipynb`](file:///C:/Users/User/Documents/2026_11_04_tvdi_python/2026_11_18/function.ipynb) 的課程內容編寫，提供繁體中文、英文、日文三種語言版本。

---

## 快速跳轉 / Quick Navigation / クイックナビゲーション
- [🇹🇼 繁體中文（Traditional Chinese）](#-繁體中文traditional-chinese)
- [🇺🇸 English](#-english)
- [🇯🇵 日本語（Japanese）](#-日本語japanese)

---

## 🇹🇼 繁體中文（Traditional Chinese）

### 1. 核心觀念：參數（Parameter）與引數（Argument）
- **參數（Parameter）**：定義函式時寫在 `def 函式名稱(...)` 括號內的變數名稱（虛擬欄位）。
- **引數（Argument）**：呼叫函式時實際傳入的值（真實資料）。

```python
# name 為「參數 (Parameter)」
def greet(name: str) -> None:
    print(f"哈囉, {name}！")

# "小明" 為「引數 (Argument)」
greet("小明")  # 輸出：哈囉, 小明！
```

---

### 2. 引數位置呼叫（Positional Arguments）
最基本的呼叫方式，引數會依照由左至右的順序依序填入參數。

```python
def describe_pet(animal: str, name: str) -> None:
    print(f"我養了一隻{animal}, 叫做{name}。")

# 依順序傳入
describe_pet("貓", "小橘")  # 輸出：我養了一隻貓, 叫做小橘。

# 順序對調時，語意會跟著改變
describe_pet("小橘", "貓")  # 輸出：我養了一隻小橘, 叫做貓。
```

---

### 3. 引數名稱呼叫（Keyword Arguments）與預設值
當參數較多時，可以直接指定 `參數名稱=值` 進行傳入，好處是不必死記順序。

```python
def describe_pet(animal: str, name: str) -> None:
    print(f"我養了一隻{animal}, 叫做{name}。")

# 名稱呼叫：順序可自由調換
describe_pet(animal="貓", name="小橘")
describe_pet(name="小橘", animal="貓")
```

#### 重要規則：混用時「位置引數」必須在「名稱引數」之前
```python
# 正確：先位置，後名稱
describe_pet("狗", name="旺財")

# 錯誤：語法錯誤（SyntaxError: positional argument follows keyword argument）
# describe_pet(animal="狗", "旺財")
```

#### 搭配預設值（Default Arguments）
定義時若設定預設值，呼叫時可省略該引數：
```python
def order_drink(drink: str, ice: str = "正常冰", sugar: str = "半糖") -> None:
    print(f"點餐: {drink} {ice}/{sugar}")

order_drink("紅茶")                          # 點餐: 紅茶 正常冰/半糖
order_drink("紅茶", "去冰")                  # 點餐: 紅茶 去冰/半糖
order_drink("紅茶", sugar="無糖")            # 點餐: 紅茶 正常冰/無糖
order_drink("紅茶", ice="少冰", sugar="微糖") # 點餐: 紅茶 少冰/微糖
```

---

### 4. 特殊符號 `/` 與 `*`：限制引數呼叫方式
Python 允許在定義函式時限制傳入方式：

| 符號 | 名稱 | 規則說明 |
| :--- | :--- | :--- |
| `/` | 僅限位置引數 (Positional-Only) | 寫在 `/` **左邊**的參數只能用位置傳入，**不能**指定參數名稱。 |
| `*` | 僅限關鍵字引數 (Keyword-Only) | 寫在 `*` **右邊**的參數**必須**指定參數名稱，不能只用位置傳入。 |

#### (1) `/` 範例（BMI 計算）
```python
def calc_bmi(weight: float, height: float, /) -> None:
    bmi = weight / (height ** 2)
    print(f"BMI為: {bmi:.1f}")

calc_bmi(65, 1.75)  # 正確，輸出：BMI為: 21.2
# calc_bmi(weight=65, height=1.75)  # 錯誤：TypeError（不能使用關鍵字）
```

#### (2) `*` 範例（發送通知信件）
```python
def send_email(to: str, *, subject: str, urgent: bool = False) -> None:
    print(f"寄給：{to}｜主旨：{subject}｜急件：{urgent}")

send_email("student@example.com", subject="課堂通知", urgent=True)
# send_email("student@example.com", "課堂通知", True)  # 錯誤：TypeError
```

#### (3) 同時包含 `/` 與 `*`
結構：`def 函式名(僅限位置, /, 位置或名稱皆可, *, 僅限名稱):`
```python
def register(id_no: str, /, name: str, *, role: str = "student") -> None:
    print(f"編號：{id_no}｜姓名：{name}｜身分：{role}")

register("A01", "小明", role="leader")       # 正確
register("A01", name="小明", role="leader")  # 正確
# register(id_no="A01", "小明")              # 錯誤：id_no 不可用名稱
```

---

### 5. `*args` 與 `**kwargs`：任意數量引數（打包 Packing）
- `*args`：把多餘的**位置引數**打包成 `tuple`。
- `**kwargs`：把多餘的**關鍵字引數**打包成 `dict`。

```python
# *args 範例
def sum_scores(*scores: int) -> int:
    print("收到的資料：", scores, type(scores))
    return sum(scores)

print(sum_scores(80, 90, 85))  # 收到的資料：(80, 90, 85) <class 'tuple'> -> 255
print(sum_scores())            # 收到的資料：() <class 'tuple'> -> 0

# **kwargs 範例
def build_profile(name: str, **info: str) -> None:
    print("姓名：", name)
    print("其他資料：", info, type(info))

build_profile("小華", city="台北", course="Python")
# 輸出：其他資料：{'city': '台北', 'course': 'Python'} <class 'dict'>
```

---

### 6. Python 內建函式實戰對照
- **`print(*objects, sep=' ', end='\n', file=None, flush=False)`**：
  `*objects` 代表接收任意數量物件；`sep` 與 `end` 在星號後面，屬於僅限關鍵字引數。
  ```python
  print('a', 'b', 1, 67, 89, sep='-')      # a-b-1-67-89
  print('a', 'b', 1, 67, 89, end='讚啦!\n') # a b 1 67 89讚啦!
  ```
- **`sorted(iterable, /, *, key=None, reverse=False)`**：
  `iterable` 為僅限位置參數；`key` 與 `reverse` 位於 `*` 後方，為僅限關鍵字引數。
  ```python
  sorted([8, 92, 63, 75], reverse=True)  # [92, 75, 63, 8]
  ```

---

## 🇺🇸 English

### 1. Core Concept: Parameters vs. Arguments
- **Parameter**: A variable name listed inside the parentheses of a function definition (`def function_name(...)`).
- **Argument**: The concrete value passed into the function when invoking/calling it.

```python
# 'name' is a Parameter
def greet(name: str) -> None:
    print(f"Hello, {name}!")

# "Alice" is an Argument
greet("Alice")  # Output: Hello, Alice!
```

---

### 2. Positional Arguments
The most common calling method. Arguments are mapped to parameters from left to right based on their relative positions.

```python
def describe_pet(animal: str, name: str) -> None:
    print(f"I have a {animal} named {name}.")

describe_pet("cat", "Luna")  # Output: I have a cat named Luna.
describe_pet("Luna", "cat")  # Output: I have a Luna named cat. (Order matters!)
```

---

### 3. Keyword Arguments & Default Parameters
Keyword arguments allow passing arguments in `parameter=value` syntax, which eliminates the need to remember exact positions and improves code readability.

```python
def describe_pet(animal: str, name: str) -> None:
    print(f"I have a {animal} named {name}.")

describe_pet(animal="cat", name="Luna")
describe_pet(name="Luna", animal="cat")  # Order does not matter
```

#### Rule: Positional arguments MUST precede keyword arguments
```python
# Valid: positional first, keyword second
describe_pet("dog", name="Buddy")

# Invalid: SyntaxError (positional argument follows keyword argument)
# describe_pet(animal="dog", "Buddy")
```

#### Default Parameter Values
Parameters with default values can be omitted during function invocation:
```python
def order_drink(drink: str, ice: str = "Regular", sugar: str = "Half") -> None:
    print(f"Order: {drink} ({ice} / {sugar})")

order_drink("Black Tea")                                  # Order: Black Tea (Regular / Half)
order_drink("Black Tea", "No Ice")                        # Order: Black Tea (No Ice / Half)
order_drink("Black Tea", sugar="Zero")                    # Order: Black Tea (Regular / Zero)
order_drink("Green Tea", ice="Less Ice", sugar="Quarter") # Order: Green Tea (Less Ice / Quarter)
```

---

### 4. Special Markers `/` and `*`: Enforcing Argument Types

| Marker | Purpose | Description |
| :--- | :--- | :--- |
| `/` | Positional-Only | Parameters to the **left** of `/` can only be passed positionally. Keyword syntax is disallowed. |
| `*` | Keyword-Only | Parameters to the **right** of `*` must be passed as keyword arguments. |

#### (1) `/` Positional-Only Example (BMI Calculation)
```python
def calc_bmi(weight: float, height: float, /) -> None:
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.1f}")

calc_bmi(65, 1.75)  # Valid: BMI: 21.2
# calc_bmi(weight=65, height=1.75)  # TypeError: positional-only arguments passed as keyword arguments
```

#### (2) `*` Keyword-Only Example (Email Dispatch)
```python
def send_email(to: str, *, subject: str, urgent: bool = False) -> None:
    print(f"To: {to} | Subject: {subject} | Urgent: {urgent}")

send_email("student@example.com", subject="Notice", urgent=True)  # Valid
# send_email("student@example.com", "Notice", True)  # TypeError
```

#### (3) Combining `/` and `*`
Syntax: `def func(positional_only, /, positional_or_keyword, *, keyword_only):`
```python
def register(id_no: str, /, name: str, *, role: str = "student") -> None:
    print(f"ID: {id_no} | Name: {name} | Role: {role}")

register("A01", "Alice", role="leader")       # Valid
register("A01", name="Alice", role="leader")  # Valid
```

---

### 5. `*args` and `**kwargs`: Variable Length Arguments (Packing)
- `*args`: Packs extra **positional arguments** into a `tuple`.
- `**kwargs`: Packs extra **keyword arguments** into a `dict`.

```python
# *args example
def sum_scores(*scores: int) -> int:
    print("Received:", scores, type(scores))
    return sum(scores)

print(sum_scores(80, 90, 85))  # Received: (80, 90, 85) <class 'tuple'> -> 255
print(sum_scores())            # Received: () <class 'tuple'> -> 0

# **kwargs example
def build_profile(name: str, **info: str) -> None:
    print("Name:", name)
    print("Additional Info:", info, type(info))

build_profile("Charlie", city="Taipei", course="Python")
# Additional Info: {'city': 'Taipei', 'course': 'Python'} <class 'dict'>
```

---

### 6. Standard Library Function Signatures
- **`print(*objects, sep=' ', end='\n', file=None, flush=False)`**:
  Accepts arbitrary positional arguments via `*objects`. `sep` and `end` come after `*objects`, meaning they are keyword-only arguments.
- **`sorted(iterable, /, *, key=None, reverse=False)`**:
  `iterable` is positional-only (before `/`); `key` and `reverse` are keyword-only (after `*`).

---

## 🇯🇵 日本語（Japanese）

### 1. 基本概念：パラメータ（仮引数）と引数（実引数）
- **パラメータ（Parameter / 仮引数）**：関数の定義時、`def 関数名(...)` の丸括弧内に宣言する変数名。
- **引数（Argument / 実引数）**：関数を呼び出す際に実際に渡す具体的な値。

```python
# name は「パラメータ (仮引数)」
def greet(name: str) -> None:
    print(f"こんにちは、{name}さん！")

# "太郎" は「引数 (実引数)」
greet("太郎")  # 出力: こんにちは、太郎さん！
```

---

### 2. 位置引数（Positional Arguments）
もっとも基本的な呼び出し形式です。引数を渡した順番（左から右）に応じて、パラメータへ順に代入されます。

```python
def describe_pet(animal: str, name: str) -> None:
    print(f"飼っている動物は{animal}で、名前は{name}です。")

# 順番通りに渡す
describe_pet("猫", "みけ")  # 出力: 飼っている動物は猫で、名前はみけです。

# 順番を逆にすると意味が変わってしまいます
describe_pet("みけ", "猫")  # 出力: 飼っている動物はみけで、名前は猫です。
```

---

### 3. キーワード引数（Keyword Arguments）とデフォルト引数
引数渡しの際に `パラメータ名=値` と明示することで、パラメータの順番を気にする必要がなくなります。

```python
def describe_pet(animal: str, name: str) -> None:
    print(f"飼っている動物は{animal}で、名前は{name}です。")

# キーワード指定のため、順序が逆でも問題ありません
describe_pet(animal="猫", name="みけ")
describe_pet(name="みけ", animal="猫")
```

#### 重要ルール：位置引数は必ずキーワード引数より前に記述する
```python
# 正しい例：位置引数を先に、キーワード引数を後に
describe_pet("犬", name="ポチ")

# 誤った例：構文エラー (SyntaxError: positional argument follows keyword argument)
# describe_pet(animal="犬", "ポチ")
```

#### デフォルト引数（Default Arguments）の活用
定義時に既定値を設定しておくことで、呼び出し時に省略可能です：
```python
def order_drink(drink: str, ice: str = "普通", sugar: str = "微糖") -> None:
    print(f"注文: {drink} (氷:{ice} / 砂糖:{sugar})")

order_drink("紅茶")                          # 注文: 紅茶 (氷:普通 / 砂糖:微糖)
order_drink("紅茶", "氷なし")                # 注文: 紅茶 (氷:氷なし / 砂糖:微糖)
order_drink("紅茶", sugar="無糖")            # 注文: 紅茶 (氷:普通 / 砂糖:無糖)
order_drink("緑茶", ice="少なめ", sugar="無糖") # 注文: 緑茶 (氷:少なめ / 砂糖:無糖)
```

---

### 4. 特殊記号 `/` と `*`：引数の渡し方を制限する

| 記号 | 制限の種類 | 説明 |
| :--- | :--- | :--- |
| `/` | 位置専用引数 (Positional-Only) | `/` より**左側**のパラメータは**位置引数のみ**で指定可能（キーワード指定不可）。 |
| `*` | キーワード専用引数 (Keyword-Only) | `*` より**右側**のパラメータは**キーワード指定が必須**（位置指定不可）。 |

#### (1) `/` の例（BMI 計算）
```python
def calc_bmi(weight: float, height: float, /) -> None:
    bmi = weight / (height ** 2)
    print(f"BMIは: {bmi:.1f}")

calc_bmi(65, 1.75)  # 正常実行 (BMIは: 21.2)
# calc_bmi(weight=65, height=1.75)  # エラー: TypeError (名前での指定は禁止)
```

#### (2) `*` の例（メール送信）
```python
def send_email(to: str, *, subject: str, urgent: bool = False) -> None:
    print(f"送信先:{to} | 件名:{subject} | 緊急:{urgent}")

send_email("student@example.com", subject="講義連絡", urgent=True)  # 正常実行
# send_email("student@example.com", "講義連絡", True)  # エラー: TypeError
```

#### (3) `/` と `*` の併用パターン
構文：`def 関数名(位置専用, /, どちらでも可, *, キーワード専用):`
```python
def register(id_no: str, /, name: str, *, role: str = "student") -> None:
    print(f"番号:{id_no} | 氏名:{name} | 役職:{role}")

register("A01", "小明", role="leader")       # 正常
register("A01", name="小明", role="leader")  # 正常
```

---

### 5. `*args` と `**kwargs`：可変長引数の受け取り（パック）
- `*args`：余分な**位置引数**を `tuple`（タプル）にまとめて受け取ります。
- `**kwargs`：余分な**キーワード引数**を `dict`（辞書）にまとめて受け取ります。

```python
# *args の例
def sum_scores(*scores: int) -> int:
    print("受け取ったデータ:", scores, type(scores))
    return sum(scores)

print(sum_scores(80, 90, 85))  # 受け取ったデータ: (80, 90, 85) <class 'tuple'> -> 255
print(sum_scores())            # 受け取ったデータ: () <class 'tuple'> -> 0

# **kwargs の例
def build_profile(name: str, **info: str) -> None:
    print("氏名:", name)
    print("その他の情報:", info, type(info))

build_profile("田中", city="東京", course="Python")
# 出力: その他の情報: {'city': '東京', 'course': 'Python'} <class 'dict'>
```

---

### 6. 標準組み込み関数の定義シグネチャ実践
- **`print(*objects, sep=' ', end='\n', file=None, flush=False)`**:
  `*objects` により任意の個数の引数を受け取り可能です。`sep` や `end` は `*objects` の後ろにあるため、キーワード指定が必須です。
- **`sorted(iterable, /, *, key=None, reverse=False)`**:
  `iterable` は `/` の前にあるため位置指定のみ。`key` と `reverse` は `*` の後ろにあるためキーワード指定が必須です。
