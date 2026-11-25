"""calc 模組的單元測試。"""

import unittest

from calc import divide


class TestDivide(unittest.TestCase):
    """測試 divide 函式。"""

    def test_divide_normal(self) -> None:
        """測試一般數值相除的結果。"""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(-9, 3), -3.0)
        self.assertAlmostEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(0, 5), 0.0)

    def test_divide_by_zero_raises_value_error(self) -> None:
        """測試除數為 0 時會拋出 ValueError 與指定錯誤訊息。"""
        for zero in (0, 0.0):
            with self.subTest(divisor=zero):
                with self.assertRaises(ValueError) as context:
                    divide(10, zero)
                self.assertEqual(str(context.exception), "除數不可為零")


if __name__ == "__main__":
    unittest.main()
