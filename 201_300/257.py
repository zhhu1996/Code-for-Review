# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        """二叉树的所有路径
        1. 深度优先遍历
        回溯到叶子节点就停止

        2. 广度优先遍历
        """
        self.result = []

        def getPath(root, path):
            if not root:
                return
            if not root.left and not root.right:
                path.append(str(root.val))
                self.result.append("->".join(path))
                path.pop()
                return
            path.append(str(root.val))
            if root.left:
                getPath(root.left, path)
            if root.right:
                getPath(root.right, path)
            path.pop()

        getPath(root, [])
        return self.result



