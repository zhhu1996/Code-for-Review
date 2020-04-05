# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 1. 递归
        # result = []
        #
        # def preOrder(root):
        #     if not root:
        #         return
        #     result.append(root.val)
        #     preOrder(root.left)
        #     preOrder(root.right)
        #
        # preOrder(root)
        # return result

        # 2. 非递归
        if not root:
            return []

        result, stack = [], []
        cur = root
        while cur or stack:
            if cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right
        return result

