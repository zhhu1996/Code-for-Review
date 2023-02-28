# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """最深叶节点的最近公共祖先
        1. 先dfs求出最大深度, 再dfs求出最深叶节点的路径, 最后根据路径求所有最深叶子节点的lca

        2. dfs求左/右子树的高度, 左子树=右子树高度, 就找到了最深叶节点的lca
        """
        # # 1.
        # self.max_depth = 0
        # self.leaf_path = []

        # def dfs_depth(root, depth):
        #     if not root: return
        #     if depth > self.max_depth:
        #         self.max_depth = depth
        #     dfs_depth(root.left, depth+1)
        #     dfs_depth(root.right, depth+1)
        
        # def dfs_path(root, depth, path):
        #     if not root: return
        #     path.append(root)
        #     if depth == self.max_depth and not root.left and not root.right:
        #         self.leaf_path.append(path.copy())
        #     dfs_path(root.left, depth+1, path)
        #     dfs_path(root.right, depth+1, path)
        #     path.pop()

        # dfs_depth(root, 0)
        # dfs_path(root, 0, [])

        # min_len = len(self.leaf_path[0])
        # leaf_cnt = len(self.leaf_path)
        # for i in range(1, len(self.leaf_path)):
        #     min_len = min(min_len, len(self.leaf_path[i]))
        # j = 0
        # while j < min_len:
        #     target = self.leaf_path[0][j]
        #     for k in range(1, leaf_cnt):
        #         if self.leaf_path[k][j] != target:
        #             return self.leaf_path[0][j-1] 
        #     j += 1
        # return self.leaf_path[0][j-1] 

        # 2.
        if not root:
            return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        if left == right:
            return root
        elif left < right:
            return self.lcaDeepestLeaves(root.right)
        else:
            return self.lcaDeepestLeaves(root.left)

    def get_height(self, root):
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))
