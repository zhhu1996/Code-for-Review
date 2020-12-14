# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """另一棵树的子树

        1. 遍历s的节点，将每个节点i与t进行比较，判断以每个节点i为根节点的子树是否与t是相同的
        """
        if not s or not t:
            return False

        def isSameTree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        def isSubtreeCore(s, t):
            if not s:
                return False
            return isSameTree(s, t) or isSubtreeCore(s.left, t) or isSubtreeCore(s.right, t)

        return isSubtreeCore(s, t)
