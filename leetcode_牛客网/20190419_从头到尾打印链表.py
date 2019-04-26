# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return []

        # 链表的长度
        count = 0
        p = listNode

        while (p != None):
            count = count + 1
            p = p.next
        # 定义数组并初始化
        arr = []
        for i in range(count):
            arr.append(0)

        # 遍历链表，将值逆向存储到数组
        q = listNode
        index = count - 1
        while (q != None):
            arr[index] = q.val
            index = index - 1
            q = q.next

        return arr

# 解法二：倒序输出，等同于栈的操作
class Solution2:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return []
        else:
            TempList = []
            LastList = []
            while listNode is not None:
                TempList.append(listNode.val)        #入栈
                listNode = listNode.next
            print("TempList:",TempList)
            while len(TempList) is not 0:
                # print(type(TempList.pop()))  <class 'int'>  int类型不能直接+=连接list
                LastList += [TempList.pop()]         #出栈  pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
                # LastList += TempList.pop()    TypeError: 'int' object is not iterable
            return LastList

class Solution3:
    def printListFromTailToHead(self, listNode):
        list = []
        while listNode:
            list.insert(0, listNode.val)  # 此处插入即是倒序的关键操作
            listNode = listNode.next
        return list



n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)

n1.next = n2
n2.next = n3
n3.next = None

# 当输入为空时，特殊情况
# test = Solution()
# ret = test.printListFromTailToHead(None)
# print(ret)

test1 = Solution()
ret1 = test1.printListFromTailToHead(n1)
print("ret1:",ret1)

test2 = Solution2()
ret2 = test2.printListFromTailToHead(n1)
print("ret2:",ret2)


test3 = Solution3()
ret3 = test2.printListFromTailToHead(n1)
print("ret3:",ret3)