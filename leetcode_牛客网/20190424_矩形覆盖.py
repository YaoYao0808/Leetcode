"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
# 超出运行时间
class Solution1:
    def rectCover(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2

        return self.rectCover(number-2) + self.rectCover(number-1)

# 超出运行时间
class Solution2:
    def __init__(self):
        self.keep = {0:0,1:1,2:2}

    def rectCover(self, number):
        num = self.rectCover(number - 2) + self.rectCover(number - 1)
        self.keep[number] = num
        return num

# 循环解决
class Solution3:
    def rectCover(self, number):
        if number <= 0:
            return 0
        list = [1,2]
        while number>=2:
            list[0],list[1] = list[1], list[0]+list[1]
            number -= 1
        return list[0]

# 循环解决
class Solution4:
    def rectCover(self, number):
        # write code here
        num=[];
        num.append(0);
        num.append(1);
        num.append(2);
        for i in range(3 , number+1):
            num.append(num[i-1]+num[i-2]);
        return num[number];
