# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """判断是否是平衡二叉树
        1. 从根节点开始，递归地对每个节点调用求树深度的函数，判断左右子树的高度差是否满足条件, 这样会有很多重复运算

        2. 从叶子节点开始后序遍历，这样每个节点的深度只需要求一次
        """

        def isBalancedCore(root):
            if not root:
                return (True, 0)
            leftBool, leftDepth = isBalancedCore(root.left)
            rightBool, rightDepth = isBalancedCore(root.right)
            if leftBool and rightBool:
                if abs(leftDepth - rightDepth) <= 1:
                    return (True, max(leftDepth, rightDepth) + 1)
            return (False, 0)

        return isBalancedCore(root)[0]