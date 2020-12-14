# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """两数之和-输入BST
        1. 递归遍历树，如果k-node.val存储在hash表中，则返回True；否则将当前节点的值存入hash表

        2. 中序遍历BST得到升序序列，然后双指针查找
        """
        self.table = {}

        def preOrder(root, target):
            if not root:
                return
            if target - root.val in self.table:
                return True
            self.table[root.val] = root
            return preOrder(root.left, target) or preOrder(root.right, target)

        return preOrder(root, k)
