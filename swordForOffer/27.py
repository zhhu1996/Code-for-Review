# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        """
        1. 递归实现前序遍历， 前序遍历的同时交换左右子树
        2. 非递归实现前序遍历，运用堆栈模拟
        """

        def getMirror(root):
            if not root:
                return None
            if root and not root.left and not root.right:
                return root
            tmp = root.left
            root.left = root.right
            root.right = tmp
            getMirror(root.left)
            getMirror(root.right)

        def getMirrorWithStack(root):
            if not root:
                return None
            stack = []
            stack.append(root)
            while stack:
                while root:
                    temp = root.left
                    root.left = root.right
                    root.right = temp
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                root = root.right

        # getMirror(root)
        getMirrorWithStack(root)
        return root

