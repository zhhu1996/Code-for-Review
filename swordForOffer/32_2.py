# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = Queue(1000)
        q.put(root)
        result = []
        thisLvNodes, nextLvNodes = 1, 0
        thisResult = []
        while not q.empty():
            node = q.get()
            thisResult.append(node.val)
            thisLvNodes -= 1
            if node.left:
                q.put(node.left)
                nextLvNodes += 1
            if node.right:
                q.put(node.right)
                nextLvNodes += 1
            if thisLvNodes == 0:
                result.append(thisResult)
                thisResult = []
                thisLvNodes = nextLvNodes
                nextLvNodes = 0
        return result
