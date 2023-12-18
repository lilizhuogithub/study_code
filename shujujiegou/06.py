# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]


# 实例化节点
n1 = ListNode(1)  # 节点 head
n2 = ListNode(3)
n3 = ListNode(2)

# 构建引用指向
n1.next = n2
n2.next = n3

c = Solution()
print(c.reversePrint(n1))
