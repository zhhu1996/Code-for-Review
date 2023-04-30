# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """路径总和III
        1. 树的搜索
        利用先序遍历搜索根节点到叶子节点的路径, 满足条件的加入集合中
        """
        ans = []

        def dfs(root, path, cumsum):
            if not root:
                return
            path.append(root.val)
            cumsum += root.val
            if not root.left and not root.right:
                if cumsum == targetSum:
                    ans.append(path.copy())
            if root.left:
                dfs(root.left, path, cumsum)
            if root.right:
                dfs(root.right, path, cumsum)
            path.pop()

        if not root: return []
        dfs(root, [], 0)
        return ans