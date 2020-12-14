# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        def preOrder(root, path, value, now):
            if not root.left and not root.right:
                path.append(root.val)
                now += root.val
                if path and now == value:
                    self.result.append(path.copy())
                path.pop()
                return
            path.append(root.val)
            if root.left:
                preOrder(root.left, path, value, now+root.val)
            if root.right:
                preOrder(root.right, path, value, now+root.val)
            path.pop()

        self.result = []
        if not root:
            return []
        preOrder(root, [], sum, 0)
        return self.result