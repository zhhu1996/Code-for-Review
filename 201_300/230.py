# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """二叉搜索树中第K小的元素
        1. 树的遍历, 时间复杂度O(n), 空间复杂度O(n)
        中序遍历BST得到递增序列, 返回第k个元素

        2. 树的搜索, 时间复杂度O(n), 空间复杂度O(1)
        遍历树的同时计数, 搜索第k小的元素
        => 可以优化到时间复杂度O(h), h=树高

        3. 非递归中序遍历, 时间复杂度O(k), 空间复杂度O(k)
        """
        # # 1.
        # ans = []

        # def dfs(root):
        #     if not root: return
        #     dfs(root.left)
        #     ans.append(root.val)
        #     dfs(root.right)
        
        # dfs(root)
        # return ans[k-1] if k <= len(ans) else -1


        # 2.
        self.pos = 0
        self.ans = -1

        def dfs(root):
            if not root: return
            dfs(root.left)
            self.pos = self.pos + 1
            if self.pos == k:
                self.ans = root.val
            dfs(root.right)
        
        dfs(root)
        return self.ans