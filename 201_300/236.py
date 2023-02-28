# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """二叉树的最近公共祖先
        1. 两次dfs搜索: dfs求根到这两个节点的路径, 再求路径间最后一个重合节点

        2. 递归
        """
        # # 1.
        # self.paths = []

        # def get_path(root, target, path):
        #     if not root: 
        #         return
        #     if root == target:
        #         path.append(target)
        #         self.paths.append(path.copy())
        #         return
        #     path.append(root)
        #     get_path(root.left, target, path)
        #     get_path(root.right, target, path)
        #     path.pop()

        # get_path(root, p, [])
        # get_path(root, q, [])
        # p_path = self.paths[0]
        # q_path = self.paths[1]
        # i = 0
        # while i < min(len(p_path), len(q_path)):
        #     if p_path[i] != q_path[i]:
        #         break
        #     i += 1
        # return p_path[i-1]

        # 2.
        if not root or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return
        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left