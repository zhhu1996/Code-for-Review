# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        """单值二叉树
        1. 先序遍历二叉树，保存每个节点的值到set中，判断set的长度是否等于1

        2. 中序遍历二叉树，保存前一个节点值，如果当前节点与前一个节点的值不相等，则返回False

        3. 递归的思想分解问题：
        以root为根节点的子树是单值的 ->
        root的左子树是单值的并且root.val == root.left.val
        root的右子树是单值的并且root.val == root.right.val
        """
        # # 方法1
        # self.pre = None
        # self.flag = True
        #
        # def inOrder(root):
        #     if not root:
        #         return
        #     inOrder(root.left)
        #     if self.pre and self.pre != root.val:
        #         self.flag = False
        #     elif not self.pre:
        #         self.pre = root.val
        #     inOrder(root.right)
        #
        # inOrder(root)
        # return self.flag

        # 方法2
        if not root:
            return True
        left = self.isUnivalTree(root.left)
        if root.left:
            left = left and (root.val == root.left.val)
        right = self.isUnivalTree(root.right)
        if root.right:
            right = right and (root.val == root.right.val)
        return left and right