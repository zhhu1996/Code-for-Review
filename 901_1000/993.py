# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """二叉树的堂兄弟节点
        1. 递归查找节点x的父节点与深度

        2. 层序遍历所有节点，将x与y的深度与父节点保存，最后进行比较

        """

        def searchTarget(root, father, depth, target):
            if not root:
                return -1, None
            if root.val == target:
                return depth, father
            left = searchTarget(root.left, root, depth + 1, target)
            right = searchTarget(root.right, root, depth + 1, target)
            if left[0] < right[0]:
                return right
            else:
                return left

        x0, x1 = searchTarget(root, None, 0, x)
        y0, y1 = searchTarget(root, None, 0, y)
        if x0 == y0 and x0 != -1 and x1 != y1:
            return True
        else:
            return False