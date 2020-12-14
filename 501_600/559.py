"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        """N叉树的最大深度"""
        if not root:
            return 0
        result = 0
        for child in root.children:
            result = max(result, self.maxDepth(child))
        return result + 1
