# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 1. 中序遍历，判断遍历序列是否有序，并且集合中不能有相等的元素
        # 二叉搜索树 <-> 中序遍历得到单调递增的元素序列
        # res = self.inOrder(root)
        # nres = list(sorted(set(res)))
        # return res == nres

        # 2. 递归地比较当前节点元素与最小元素，最大元素
        return self.validBST(root, -2 ** 31 - 1, 2 ** 31)

    def validBST(self, root, amin, amax):
        # 比较当前节点是否满足二叉搜索树的要求，当前节点必须在(amin, amax)范围内
        if not root:
            return True

        if root.val <= amin or root.val >= amax:  # 等号必须要有
            return False

        return self.validBST(root.left, amin, root.val) and self.validBST(root.right, root.val, amax)

    def inOrder(self, root):
        # 返回中序遍历的list
        if not root:
            return []

        result = []
        result += self.inOrder(root.left)
        result.append(root.val)
        result += self.inOrder(root.right)

        return result
