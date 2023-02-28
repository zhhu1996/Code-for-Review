# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """ 二叉树中的链表
        1. 遍历树-判断结构
        """
        def is_equal(root, head):
            if not head:
                return True
            if not root or root.val != head.val:
                return False
            return is_equal(root.left, head.next) or is_equal(root.right, head.next)

        def is_subpath(head, root):
            if not root:
                return False
            return is_equal(root, head) or is_subpath(head, root.left) or is_subpath(head, root.right)

        return is_subpath(head, root)
            