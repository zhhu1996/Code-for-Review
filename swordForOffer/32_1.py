# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = Queue(1000)
        q.put(root)
        result = []
        while not q.empty():
            node = q.get()
            result.append(node.val)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return result