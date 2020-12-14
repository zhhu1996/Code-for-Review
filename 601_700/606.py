# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        """根据二叉树创建字符串
        1. 左子树非空，则在遍历左子树前加上(,结束左子树的遍历后加上);
           左子树为空，但是右子树非空，必须要加上();
           右子树非空，遍历右子树前加上(,结束右子树的遍历后加上);
        """
        self.result = []

        def preOrder(root):
            if not root:
                return
            self.result.append(str(root.val))
            if root.left:
                self.result.append("(")
                preOrder(root.left)
                self.result.append(")")
            if not root.left and root.right:
                self.result.append("(")
                self.result.append(")")
            if root.right:
                self.result.append("(")
                preOrder(root.right)
                self.result.append(")")

        preOrder(t)
        return "".join(self.result)