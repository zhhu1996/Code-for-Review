# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        """分裂二叉树的最大乘积
        首先求树全部节点的和totalSum，之后对于树的每个子树结构，求解子树和value与其余和的乘积
        """

        def getTotalSum(root):
            if not root:
                return 0
            lValue = getTotalSum(root.left)
            rValue = getTotalSum(root.right)
            return root.val + lValue + rValue

        self.totalSum = getTotalSum(root)
        self.result = 0

        def getMaxProduct(root):
            if not root:
                return 0
            value = root.val + getMaxProduct(root.left) + getMaxProduct(root.right)
            self.result = max(value * (self.totalSum-value), self.result)
            return value

        getMaxProduct(root)
        return self.result % (10**9 + 7)