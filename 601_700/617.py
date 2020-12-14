# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """合并二叉树
        1. 递归地合并左子树、根、右子树
        if 两个节点都非空，则将节点值相加并递归地处理左子树和右子树，最后返回当前节点;
        if t1为空，t2非空，则直接返回t2;
        if t1非空，t2为空，则直接返回t1;
        if t1、t2为空，则返回空
        """
        if t1 and t2:
            node = TreeNode(t1.val+t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node
        elif not t1 and t2:
            return t2
        elif t1 and not t2:
            return t1
        else:
            return None