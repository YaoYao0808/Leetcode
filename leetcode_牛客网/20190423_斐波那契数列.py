"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""

class Solution1:
    # 递归解法显示超时
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.Fibonacci(n-1)+self.Fibonacci(n-2)


class Solution2:
    def __init__(self):
        self.keep = {0:0, 1:1}
    # 用字典存储计算过的值，避免重复计算
    def Fibonacci(self, n):
        if n in self.keep:
            return self.keep[n]
        else:
            fn = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
            self.keep[n] = fn
            return fn

# 如果不使用递归，而是直接使用前两个数字的和相加得到第三个数字的方式能把时间复杂度降到O（n）。
class Solution3:
    def Fibonacci(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a


test2 = Solution2()
ret = test2.Fibonacci(4)
print("ret:",ret)

