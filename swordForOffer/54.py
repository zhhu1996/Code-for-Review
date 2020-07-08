# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """二叉搜索树的第k大节点
        1. 中序遍历，得到递增的数组，直接查找即可，需要O(n)的空间

        2. 按照右、根、左的顺序遍历，同时判断是否是第k大的节点
        """
        if not root or k <= 0:
            return -1
        self.k = k

        def kthLargestCore(root):
            target = None
            if root.right:
                target = kthLargestCore(root.right)
            if not target:
                if self.k == 1:
                    target = root
                self.k -= 1
            if not target and root.left:
                target = kthLargestCore(root.left)
            return target

        return kthLargestCore(root).val
