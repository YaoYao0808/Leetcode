"""
题目描述：
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

此题在Python中两种解法：
1，使用python中自带的方法bin()，将数字转化为二进制，然后统计其1的个数
2.n&(n-1)，直到为0，注意条件为：while n & 0xffffffff != 0，因为要考虑到负数

"""
class Solution1:
    def NumberOf1(self, n):
        if n >= 0:
            return bin(n).count('1')
        else:# 若为负数，则 n & 0xffffffff 得到其负数的二进制表示
            return bin(n & 0xffffffff).count('1')

class Solution2:
    """"
    下述做法只是适用于n为正数的情况
    def NumberOf1(self, n):
        count = 0
        while n != 0:
            count += 1
            n = n & (n - 1)
        return count
    """
    def NumberOf1(self, n):
        count = 0
        while n & 0xffffffff != 0:
            count += 1
            n = n & (n - 1)
        return count

class Func:
    def test_bin(self,n):
        # bin()是将整型转换为二进制数组成的字符串
        str = bin(n)
        # print("type:",type(str))  type: <class 'str'>
        return str

testFunc = Func()
ret = testFunc.test_bin(7)
print("ret:",ret)  #0b111




