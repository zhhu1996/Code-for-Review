"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """N叉树的前序遍历
        1. 递归

        2. 迭代: 由二叉树的前序遍历扩展
        """
        self.result = []

        def preOrderCore(root):
            if not root:
                return
            self.result.append(root.val)
            for child in root.children:
                preOrderCore(child)

        def preOrderCoreV2(root):
            if not root:
                return []
            stack = [root]
            while stack:
                node = stack.pop()
                self.result.append(node.val)
                for i in range(len(node.children)-1, -1, -1):
                    stack.append(node.children[i])

        # preOrderCore(root)
        preOrderCoreV2(root)
        return self.result
