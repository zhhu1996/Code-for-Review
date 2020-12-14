# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        """从根到叶的二进制数之和
        1. 保存所有根到叶子节点的路径到列表中，对列表中的所有路径求和

        2. 在求路径的时候其实就可以计算当前的值了
        """
        # 方法2
        self.totalSum = 0

        def dfs(root, now):
            if not root:
                return
            if not root.left and not root.right:
                now = now * 2 + root.val
                self.totalSum += now
                return
            now = now * 2 + root.val
            dfs(root.left, now)
            dfs(root.right, now)

        dfs(root, 0)
        return self.totalSum