"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """填充每个节点的下一个右侧节点指针 II
        1. bfs, 时间复杂度O(n), 空间复杂度O(logn)

        2. 遍历, 时间复杂度O(n), 空间复杂度O(1)
        """
        # # 1.
        # from queue import Queue
        
        # if not root:
        #     return None
        # q = Queue(-1)
        # q.put(root)
        # while not q.empty():
        #     size = q.qsize()
        #     pre = None
        #     for i in range(size):
        #         cur = q.get()
        #         cur.next = pre
        #         pre = cur
        #         if cur.right:
        #             q.put(cur.right)
        #         if cur.left:
        #             q.put(cur.left)
        # return root


        # 2.
        if not root:
            return None
        cur = root
        while cur:
            dummy = Node(-1)
            pre = dummy
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next
            cur = dummy.next
        return root