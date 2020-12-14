"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        """N叉树的克隆
        1. 层序遍历，逐个克隆

        2. 深度优先遍历，对于每个节点的克隆，相当于节点值的初始化，孩子节点的克隆
        """
        if not root:
            return None
        node = Node(root.val)
        node.children = []
        for child in root.children:
            node.children.append(self.cloneTree(child))
        return node