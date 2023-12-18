# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(node):
            if not node: return None

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        res = []
        dfs(root)

        return res[-k]


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


c = Solution()
print(c.kthLargest(root, 3))



