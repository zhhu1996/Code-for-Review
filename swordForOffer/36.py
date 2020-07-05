"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """把树分为3部分，左子树、根、右子树, 递归处理左子树，并把左子树最大的节点与根节点连接起来，之后递归处理右子树
        注意，python中如果想在函数中更新可变对象的引用(=是不会返回的！)，则只能设置全局变量或者类成员变量
        """

        def convertNode(root):
            current = root
            if current.left:
                convertNode(current.left)
            current.left = self.lastNode
            if self.lastNode:
                self.lastNode.right = current
            self.lastNode = current
            if current.right:
                convertNode(current.right)

        self.lastNode = None
        if not root:
            return None
        convertNode(root)
        # 连接头节点和尾节点
        headNode = self.lastNode
        while headNode and headNode.left:
            headNode = headNode.left
        headNode.left = self.lastNode
        self.lastNode.right = headNode
        return headNode