# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """左叶子之和
        1. 递归遍历树，记录当前节点的父节点。每到一个节点，判断是否是叶子节点，是否是左孩子，满足条件就相加

        2. 不设置全局变量，递归地计算值
        """
        ## 方法1
        # self.totalSum = 0
        # def getSum(root, pre):
        #     if not root:
        #         return
        #     if not root.left and not root.right and pre and pre.left == root:
        #         self.totalSum += root.val
        #         return
        #     getSum(root.left, root)
        #     getSum(root.right, root)
        #
        # getSum(root, None)
        # return self.totalSum

        # 方法2
        def getSum(root, pre):
            if not root:
                return 0
            now = 0
            if not root.left and not root.right and pre and pre.left == root:
                now += root.val
            return now + getSum(root.left, root) + getSum(root.right, root)

        return getSum(root, None)
