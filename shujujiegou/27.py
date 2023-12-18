import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def mirrorTree(self, root: TreeNode) -> TreeNode:
#         if not root: return
#         # tmp = root.left
#         # root.left = self.mirrorTree(root.right)
#         # root.right = self.mirrorTree(tmp)
#         root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
#         return root
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root


# 构建二叉树
#              3
#             / \
#            9  20
#              /  \
#             15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

c = Solution()
print(c.mirrorTree(root))
print(root.right.val)





