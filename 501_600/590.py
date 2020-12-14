"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """N叉树的后序遍历
        1. 递归
        先访问孩子节点，再根节点

        2. 迭代
        """
        # # 方法1
        # self.result = []
        #
        # def postOrderCore(root):
        #     if not root:
        #         return
        #     for child in root.children:
        #         postOrderCore(child)
        #     self.result.append(root.val)
        #
        # postOrderCore(root)
        # return self.result

        # 方法2
        if not root:
            return
        result = []
        stack = [root]
        while stack:
            now = stack.pop()
            result.append(now.val)
            for child in now.children:
                stack.append(child)
        return result[::-1]
