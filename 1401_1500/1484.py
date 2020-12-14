# Definition for a binary tree node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random
from queue import Queue

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        """克隆含随机指针的二叉树
        1. 先处理left指针和right指针，建立一颗新树，并建立原节点与新节点的映射，用层序遍历比较方便；之后处理random指针，根据映射关系直接找到
        应指向的节点

        2.
        """
        # # 方法1
        # if not root:
        #     return None
        # q1, q2 = Queue(1000), Queue(1000)
        # nRoot = NodeCopy(root.val)
        # q1.put(root)
        # q2.put(nRoot)
        # table = {}
        # while not q1.empty():
        #     node1 = q1.get()
        #     node2 = q2.get()
        #     table[node1] = node2
        #     if node1.left:
        #         nleft = NodeCopy(node1.left.val)
        #         q1.put(node1.left)
        #         node2.left = nleft
        #         q2.put(nleft)
        #     if node1.right:
        #         nright = NodeCopy(node1.right.val)
        #         q1.put(node1.right)
        #         node2.right = nright
        #         q2.put(nright)
        # if not q1.empty():
        #     q1 = Queue(1000)
        # if not q2.empty():
        #     q2 = Queue(1000)
        # q1.put(root)
        # q2.put(nRoot)
        # while not q1.empty():
        #     node1 = q1.get()
        #     node2 = q2.get()
        #     if node1.random:
        #         node2.random = table[node1.random]
        #     if node1.left:
        #         q1.put(node1.left)
        #     if node1.right:
        #         q1.put(node1.right)
        #     if node2.left:
        #         q2.put(node2.left)
        #     if node2.right:
        #         q2.put(node2.right)
        # return nRoot

        # 方法2
        if not root:
            return None
        self.table = {}

        def dfs(root):
            if root in self.table:
                return self.table[root]
            node = NodeCopy(root.val)
            self.table[root] = node
            if root.left:
                node.left = dfs(root.left)
            if root.right:
                node.right = dfs(root.right)
            if root.random:
                node.random = dfs(root.random)
            return node

        return dfs(root)
