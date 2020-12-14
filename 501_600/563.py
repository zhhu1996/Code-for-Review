# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        """二叉树的坡度
        1. 递归
        递归计算二叉树左子树的节点之和、右子树的节点之和，得到当前节点的坡度，返回当前节点的和
        """
        self.totalSum = 0

        def getTreeSum(root):
            """返回root子树的所有节点之和"""
            if not root:
                return 0
            left = getTreeSum(root.left)
            right = getTreeSum(root.right)
            self.totalSum += abs(left-right)
            return left + right + root.val

        getTreeSum(root)
        return self.totalSum