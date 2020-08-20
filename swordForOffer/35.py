"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """复杂链表的复制
        1. 先复制next指针，再复制random指针
            next指针：遍历愿链表，并生成hash表存储两个节点之间的对应关系
            random指针：再次遍历链表random指针应该指向哪里
        """
        if not head:
            return None
        table = {}
        # 先复制第一个节点
        head2 = Node(head.val)
        table[head] = head2
        cur1 = head.next
        cur2 = head2
        # 遍历原链表，生成每个节点内容
        while cur1:
            # next指针
            newNode = Node(cur1.val)
            table[cur1] = newNode
            cur2.next = newNode
            cur2 = cur2.next
            cur1 = cur1.next
        cur1 = head
        cur2 = head2
        while cur1:
            if cur1.random:
                cur2.random = table[cur1.random]
            cur1 = cur1.next
            cur2 = cur2.next
        return head2