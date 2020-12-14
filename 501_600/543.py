# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """二叉树的直径
        根节点的路径 = max(左子树的路径，右子树的路径) + 2
        因为路径长度 = 路径包含的节点个数 - 1， 所以问题可转化为求路径上的节点个数
        """
        self.result = 0

        def getNodeLength(root):
            if not root:
                return -1
            left = getNodeLength(root.left)
            right = getNodeLength(root.right)
            self.result = max(self.result, left+right+2)
            return max(left, right) + 1

        getNodeLength(root)
        return self.result