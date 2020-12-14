# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        """二叉搜索树的范围和
        1. 递归遍历

        2. 非递归
        """
        self.result = 0

        def preOrder(root, l, r):
            if not root:
                return
            if root.val >= l and root.val <= r:
                self.result += root.val
            if root.val < l:
                preOrder(root.right, l, r)
            elif root.val > r:
                preOrder(root.left, l, r)
            else:
                preOrder(root.left, l, r)
                preOrder(root.right, l, r)

        preOrder(root, L, R)
        return self.result
