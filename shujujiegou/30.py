import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        i = 1
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            # if i % 2 == 1:
            #     res.append(tmp)
            # else:
            #     res.append(tmp[::-1])
            res.append(tmp if i % 2 else tmp[::-1])
            i = i + 1
        return res

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
print(c.levelOrder(root))