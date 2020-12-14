# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        """叶子相似的树
        1. 分别先序遍历，保存叶子节点到列表中，然后比较两个列表是否相等

        """

        def preOrder(root, path):
            if not root:
                return
            if not root.left and not root.right:
                path.append(root.val)
            preOrder(root.left, path)
            preOrder(root.right, path)

        result1, result2 = [], []
        preOrder(root1, result1)
        preOrder(root2, result2)
        return result1 == result2
