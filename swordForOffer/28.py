# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """对称二叉树
        1. 先求出镜像，然后遍历比较
        2. 重写遍历函数，前序遍历和对称前序遍历
        """

        def isEqual(node1, node2):
            if not node1 and not node2: # 考虑了空节点
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return isEqual(node1.left, node2.right) and isEqual(node1.right, node2.left)

        return isEqual(root, root)