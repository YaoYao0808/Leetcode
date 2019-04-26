"""
题目描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""
class Solution1:
    # 递归做法超时
    def jumpFloor(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        return self.jumpFloor(number-1)+self.jumpFloor(number-2)

class Solution2:
    # 采用字典存储计算过的值，这也可以避免重复计算
    def __init__(self):
        self.keep = {1:1,2:2,3:3}

    def jumpFloor(self,number):
        if number  in self.keep:
            return self.keep[number]
        else:
            fn = self.jumpFloor(number-1)+self.jumpFloor(number-2)
            self.keep[number] = fn
            return fn

"""
升级版的青蛙跳台阶
题目描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
# f (n) = f (n-1) + f (n-2) + f (n-3) + … + f (2) + f (1)
"""
f(1) = 1

f(2) = f(2-1) + f(2-2)         //f(2-2) 表示2阶一次跳2阶的次数。

f(3) = f(3-1) + f(3-2) + f(3-3) 

f(4) = f(4-1) + f(4-2) + f(4-3) + f(4-4)  
...

f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f(n-(n-1)) + f(n-n) 

所以：f (n) = f (n-1) + f (n-2) + f (n-3) + … + f (2) + f (1)
"""
class Solution3:
    def jumpFloorII(self, number):
        # write code here
        if number < 3: # {1:1,2:2,3:4}
            return number
        a = [0,1,2]
        for i in range(3, number+1):
            a.append(sum(a)+1)  # f(0)也算是一种解法
        print(a)
        return a[number]

test3 = Solution3()
ret = test3.jumpFloorII(4)
print("ret:",ret)






