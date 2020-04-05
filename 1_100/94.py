# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # # 1. 递归
        # result = []
        #
        # def inOrder(root):
        #     if not root:
        #         return
        #     inOrder(root.left)
        #     result.append(root.val)
        #     inOrder(root.right)
        #
        # inOrder(root)
        # return result

        # 2. 非递归
        if not root:
            return []
        stack, result = [], []
        cur = root
        while cur or stack:  # 当遍历指针不为空或者堆栈还有元素时，就需要继续循环
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result
