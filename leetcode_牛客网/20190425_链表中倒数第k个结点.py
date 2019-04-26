"""
题目描述：

输入一个链表，输出该链表中倒数第k个结点。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法一：传统思维，先求出链表中节点的个数，再求倒数第k个结点
class Solution1:
    def FindKthToTail(self, head, k):
        count = 0
        p = head
        while p!=None:
            count = count + 1
            p = p.next

        if count < k:
            return None

        print("count:",count)

        # 第(count - k + 1)个节点，就是倒数第k个结点  4

        index = 1
        q = head
        while index<count-k+1:
            q = q.next
            index = index + 1

        return  q

class Solution2:
    def FindKthToTail(self, head, k):
        # p,q = head
        p = head
        q = head

        for i in range(k):
            # 如果k大于链表长度，返回空
            if p == None:
                return None
            p = p.next

        while p!=None:  # 注意此处的判断，p!=None
            p = p.next
            q = q.next

        return q


class Solution4:
    def FindKthToTail(self, head, k):
        p = head
        q = head

        if head is None:  #  此处判断可不要
            return None

        count = 1

        while count <= k:
            if p is None:
                return None
            p = p.next
            count = count + 1

        while p != None:
            p = p.next
            q = q.next

        return q





n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = None

test1 = Solution1()
ret1 = test1.FindKthToTail(n1,1)
print("ret1:",ret1)

test2 = Solution2()
ret2 = test2.FindKthToTail(n1,1)
print("ret2:",ret2)

test3 = Solution3()
ret3 = test3.FindKthToTail(n1,3)
print("ret3:",ret3)