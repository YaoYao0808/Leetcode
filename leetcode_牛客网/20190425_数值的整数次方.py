"""
题目描述：
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""

# 常规的循环解法
class Solution1:
    def Power(self, base, exponent):
        if exponent < 1:
            return 1 / self.getPower(base, -exponent)
        else:
            return self.getPower(base, exponent)

    def getPower(self, base, exponent):
        if base == 0:
            return 0
        elif exponent == 1:
            return base
        res = 1
        for i in range(exponent):
            res *= base
        return res

