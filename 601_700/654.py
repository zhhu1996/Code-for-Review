# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """最大二叉树
        1. 递归建树

        2. 非递归建树(单调栈)
        位置i的树节点val[i], 需要比左子树和右子树的最大值都要大
        => val[i]的左节点是比val[i]小的最大值
        => 比val[i]大的最小值的右节点是val[i]
        """
        # # 1.  
        # if not nums:
        #     return None
        # l, r = 0, len(nums)-1
        # index = -1
        # max_res = -float('inf')
        # for i in range(l, r+1):
        #     if nums[i] > max_res:
        #         max_res = nums[i]
        #         index = i
        # root = TreeNode(nums[index])
        # root.left = self.constructMaximumBinaryTree(nums[l:index])
        # root.right = self.constructMaximumBinaryTree(nums[index+1:r+1])
        # return root

        # 2.
        s = []
        for num in nums:
            node = TreeNode(num)
            while s and s[-1].val < num:
                node.left = s[-1]
                s.pop()
            if s:
                s[-1].right = node
            s.append(node)
        return s[0]