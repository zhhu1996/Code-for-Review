# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 1. 递归
        # result = []
        #
        # def postOrder(root):
        #     if not root:
        #         return
        #     postOrder(root.left)
        #     postOrder(root.right)
        #     result.append(root.val)
        #
        # postOrder(root)
        # return result

        # 2. 非递归： 前序遍历根、右、左，然后逆序输出
        if not root:
            return []

        result, stack = [], []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                result.append(cur.val)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left
        return result[::-1]

        # 3. 非递归：前序遍历的思想，设立一个pre指针指向上一个访问的节点
