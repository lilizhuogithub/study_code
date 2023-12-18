class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


A = TreeNode(3)
A.left = TreeNode(4)
A.right = TreeNode(5)
A.left.left = TreeNode(1)
A.left.right = TreeNode(2)
B = TreeNode(4)
B.left = TreeNode(1)

c = Solution()
c.isSubStructure(A, B)
