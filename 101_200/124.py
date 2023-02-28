# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """二叉树中的最大路径和
        1. 遍历问题
        i. 根作为路径的端点
        ii.根作为区间内的点
        """
        self.res = -float('inf')
        
        def search(root):
            if not root:
                return 0
            left = search(root.left)
            right = search(root.right)
            # 根为端点
            cur = root.val
            if left > 0:
                cur += left
            if right > 0:
                cur += right
            self.res = max(self.res, cur)
            # 根为区间
            cur = root.val
            cur += max(left, right, 0)
            return cur
        
        cur = search(root)
        return self.res if self.res > cur else cur