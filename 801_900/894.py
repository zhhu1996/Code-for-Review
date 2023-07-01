# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cache = {}

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        """所有可能的真二叉树
        1. 递归 + 记忆化
        f(n) = f(1)*f(n-2) + f(3)*f(n-4) + ... + f(n-2)*f(1)
        """
        if n in self.cache:
            return self.cache[n]
        if n == 1:
            return [TreeNode(0)]
        if n % 2 == 0:
            return []
        ans = []
        for l_cnt in range(1, n, 2):
            r_cnt = n - l_cnt - 1
            l_node = self.allPossibleFBT(l_cnt)
            r_node = self.allPossibleFBT(r_cnt)
            for l in l_node:
                for r in r_node:
                    root = TreeNode(0, l, r)
                    ans.append(root)
        self.cache[n] = ans
        return ans