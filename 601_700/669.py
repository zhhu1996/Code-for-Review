# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        """二叉搜索树的修建
        1.
        如果当前节点为空，返回None
        如果当前节点的值 < L，则返回右子树
        如果当前节点的值 > R，则返回左子树
        如果当前节点的值在[L,R]之间，则递归调用
        """

        def trimTree(root, L, R):
            """返回以root为根节点的子树的修建结果"""
            if not root:
                return None
            if root.val < L:
                return trimTree(root.right)
            if root.val > R:
                return trimTree(root.left)
            root.left = trimTree(root.left, L, R)
            root.right = trimTree(root.right, L, R)
            return root

        return trimTree(root, L, R)