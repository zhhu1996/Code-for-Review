# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        """寻找所有的独生节点
        1. 深度优先遍历

        2. 宽度优先遍历
        """
        self.result = []

        def preOrder(root):
            if not root:
                return
            if not root.left and root.right:
                self.result.append(root.right.val)
            if root.left and not root.right:
                self.result.append(root.left.val)
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)
        return self.result