# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur: return pre  # 终止条件
            res = recur(cur.next, cur)  # 递归后继节点
            cur.next = pre  # 修改节点引用指向
            return res  # 返回反转链表的头节点

        return recur(head, None)  # 调用递归并返回

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         cur, pre = head, None
#         while cur:
#             cur.next, pre, cur = pre, cur, cur.next
#         return pre

# 实例化节点
n1 = ListNode(1)  # 节点 head
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
# 构建引用指向
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

c = Solution()
print(c.reverseList(n1))
# 测试链表是否反转
print(n4.val)
print(n4.next.val)