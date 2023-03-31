# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """完全二叉树的节点个数
        1. BFS/DFS, 时间复杂度O(n)

        2. 二分, 时间复杂度O(logn*logn)
        """
        # # 1.
        # def dfs(root):
        #     if not root: return 0
        #     l = dfs(root.left)
        #     r = dfs(root.right)
        #     return 1 + l + r
        
        # return dfs(root)


        # 2.
        if not root:
            return 0
        lh = self.countLevel(root.left)
        rh = self.countLevel(root.right)
        if lh == rh:
            return 2**lh + self.countNodes(root.right)
        else:
            return 2**rh + self.countNodes(root.left)

    def countLevel(self, root):
        h = 0
        while root:
            h += 1
            root = root.left
        return h