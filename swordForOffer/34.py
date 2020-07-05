# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        def preOrder(root, path, value):
            path.append(root.val)
            if not root.left and not root.right:
                if path:
                    pathSum = 0
                    for x in path:
                        pathSum += x
                    if pathSum == value:
                        self.result.append(path.copy())
            if root.left:
                preOrder(root.left, path, value)
            if root.right:
                preOrder(root.right, path, value)
            path.pop()

        self.result = []
        if not root:
            return []
        preOrder(root, [], sum)
        return self.result