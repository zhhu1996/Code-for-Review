# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """将有序数组转换成二叉搜索树
        1. 递归
        每次取nums的中点作为BST的根节点, 左边和右边的元素递归进行建树
        """
        if not nums:
            return None
        mid = (len(nums)-1) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root