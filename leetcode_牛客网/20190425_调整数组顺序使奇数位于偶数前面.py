"""
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""

# 解法一：快速排序的变形  解法不通过
# 存在的问题：快速排序为不稳定算法，因此会改变相对位置
class Solution1:
    def reOrderArray(self, array):
        len = len(array)
        i = 0
        j = len-1

        while i<j:
            while i<j and (array[i]%2!=0):
                i = i+1
            while i<j and (array[j]%2==0):
                j = j-1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

        return array


# [1,2,3,4,5,6,7] --> [1,3,5,7,2,4,6]
# 解法二：传统的方法，定义一个新的数组，两次遍历，第一次存储奇数，第二次存储偶数
# 空间复杂度为O(n)，时间复杂度为0(n)
class Solution2:
    def reOrderArray(self, array):
        len_array = len(array)
        arr_temp = []

        for i in range(len_array):
            arr_temp.append(0)   # [0, 0, 0, 0, 0, 0, 0]

        count = 0 # 奇数的个数
        for i in range(len_array):
            if array[i]%2!=0:
                arr_temp[count] = array[i]
                count = count + 1

        index = count
        for i in range(len_array):
            if array[i]%2==0:
                arr_temp[index] = array[i]
                index = index + 1

        return arr_temp


# 解法三：思路同解法二相同，区别在于判断奇偶数的方法不一样，a & 1=1为奇数，a & 1=0为偶数
class Solution3:
    def reOrderArray(self, array):
        def isOdd(a):
            return (a & 1) == 1
        answer = [i for i in array if isOdd(i)]
        answer.extend([i for i in array if not isOdd(i)])
        return answer

# 解法四：灵活运用sorted方法
class Solution4:
    def reOrderArray(self, array):
        return sorted(array, key = lambda x: x % 2 == 0)  # True为倒序排列，False为正序排列


test2 = Solution2()
ret2 = test2.reOrderArray([1,2,3,4,5,6,7] )
print("ret2:",ret2)

test4 = Solution4()
ret4 = test4.reOrderArray([1,2,3,4,5,6,7] )
print("ret4:",ret4)