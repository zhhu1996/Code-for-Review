# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        """在二叉树中分配硬币
        """
        self.move = 0

        def need_coins(root):
            if not root: return 0
            left = need_coins(root.left)
            right = need_coins(root.right)
            cur = root.val
            self.move += abs(left) + abs(right)
            return cur - 1 + left + right

        assert need_coins(root) == 0
        return self.move