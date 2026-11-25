"""簡易計算模組。"""


def divide(a: int | float, b: int | float) -> float:
    """計算 a 除以 b 的商，當除數為 0 時拋出 ValueError。"""
    if b == 0:
        raise ValueError("除數不可為零")
    return a / b
