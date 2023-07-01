# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        """翻转二叉树以匹配先序遍历
        1. dfs
        遍历节点, 根据左孩子与待匹配的节点判断是否需要判断左/右子树
        翻转并不需要调整指针, 直接修改遍历顺序即可 
        """
        self.index = 0
        self.ans = []

        def dfs(root):
            # 判断以root为根的节点是否需要翻转左/右子树
            if not root:
                return
            if root.val == voyage[self.index]:
                self.index += 1
            else:
                self.ans = [-1]
                return
            if self.index < len(voyage) and root.left and root.left.val != voyage[self.index]:
                self.ans.append(root.val)
                dfs(root.right)
                dfs(root.left)
            else:
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        return self.ans if self.index == len(voyage) else [-1]   