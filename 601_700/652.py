# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """寻找重复的子树
        1. 序列化 + 哈希表
        """
        from collections import defaultdict
        self.map = defaultdict(int)
        self.ans = []

        def dfs(root):
            # 序列化root子树
            if not root: return ' '
            left = dfs(root.left)
            right = dfs(root.right)
            # 前序满足
            # s = str(root.val) + ',' + left + ',' + right
            # 中序不满足
            # 后序满足
            s = left + ',' + right + ',' + str(root.val)
            self.map[s] += 1
            if self.map[s] == 2:
                self.ans.append(root)
            return s

        dfs(root)
        return self.ans