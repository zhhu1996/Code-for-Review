# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        def hasSubTree(node1, node2):
            """node1子树是否包含node2子树"""
            if not node2:
                return True
            if not node1:
                return False
            if node1.val != node2.val:
                return False
            return hasSubTree(node1.left, node2.left) and hasSubTree(node1.right, node2.right)

        def preOrder(node1, node2):
            """前序遍历node1子树，并与node2节点进行比较"""
            flag = False
            if node1 and node2:
                if node1.val == node2.val:
                    flag = hasSubTree(node1, node2)
                if not flag:
                    flag = preOrder(node1.left, node2)
                if not flag:
                    flag = preOrder(node1.right, node2)
            return flag

        return preOrder(A, B)
