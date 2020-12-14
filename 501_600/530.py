# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        """二叉搜索树的最小绝对差
        1. 中序遍历，计算当前节点与前一个节点的差值的绝对值

        """
        # 方法1
        self.pre = None
        self.minValue = float("inf")

        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            if self.pre:
                self.minValue = min(self.minValue, abs(self.pre.val-root.val))
            self.pre = root
            inOrder(root.right)

        inOrder(root)
        return self.minValue