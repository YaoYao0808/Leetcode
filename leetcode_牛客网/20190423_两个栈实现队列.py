"""
栈：后进先出
队列：先进先出

list：pop是移除并返回最后一个元素
stack1,stack2，stack2作中转栈
插入操作push时：
    假设stack1的内存空间足够大，因此直接stack1.append()即可
删除操作pop时：
    stack2和stack1都为空时，返回空
    stack2不为空则直接移除
    stack2为空时：stack1不为空，则弹出stack1的元素加入到stack2,再弹出stack2
"""
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if not self.stack1 and not self.stack2:
            return []

        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

test = Solution()
# test.push(5)
ret = test.pop()
print(ret)


