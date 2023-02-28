# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """最大二叉树 II
        1. 迭代法

        2. 递归法
        """
        # 1.
        # node = TreeNode(val)
        # if val > root.val:
        #     node.left = root
        #     return node
        # pre = root
        # cur = root.right
        # while cur:
        #     if val > cur.val:
        #         node.left = cur
        #         pre.right = node
        #         break
        #     else:
        #         pre = cur
        #         cur = cur.right
        # if not cur:
        #     pre.right = node
        # return root

        # 2.
        if root.val < val:
            node = TreeNode(val)
            node.left = root
            return node
        if not root.right:
            root.right = TreeNode(val)
            return root
        root.right = self.insertIntoMaxTree(root.right, val)
        return root