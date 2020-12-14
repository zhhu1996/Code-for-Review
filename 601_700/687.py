# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        """最长同值路径
        1. 遍历每个节点，从当前节点开始，分别向左子树分叉和向右子树分叉，求包含当前节点的最长同值路径（注意只有根节点才可以分叉，内部节点不行）
        """
        self.maxLUP = 0

        def getLongestUniqueV(root):
            if not root:
                return 0
            left = getLongestUniqueV(root.left)
            right = getLongestUniqueV(root.right)
            leftArrow, rightArrow = 0, 0
            if root.left and root.val == root.left.val:
                leftArrow = left + 1
            if root.right and root.val == root.right.val:
                rightArrow = right + 1
            self.maxLUP = max(self.maxLUP, leftArrow + rightArrow)
            return max(leftArrow, rightArrow)

        getLongestUniqueV(root)
        return self.maxLUP
