# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        """最接近的二叉搜索树的值
        1. 递归，递归遍历每个节点，保存最小值
        2. 非递归，
        """
        self.closeNode = None

        def searchV1(root, target):
            if not root:
                return
            if not self.closeNode:
                self.closeNode = root
            if self.closeNode and abs(self.closeNode.val - target) > abs(root.val - target):
                self.closeNode = root
            if root.val == target:
                self.closeNode = root
            elif root.val < target:
                search(root.right, target)
            else:
                search(root.left, target)

        def searchV2(root, target):
            if not root:
                return
            self.closeNode = root
            while root and root.val != target:
                if abs(self.closeNode.val - target) > abs(root.val - target):
                    self.closeNode = root
                if root.val > target:
                    root = root.left
                else:
                    root = root.right
            if root and root.val == target:
                return root
            return self.closeNode

        # searchV1(root, target)
        return searchV2(root, target).val
        # return self.closeNode.val