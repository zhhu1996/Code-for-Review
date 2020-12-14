from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        """二叉搜索树的众数
        1. 用hash表存储每个数出现的次数，时间复杂度O(n)，空间复杂度O(n)

        2. 二叉搜索树的中序遍历是递增序列，中序遍历二叉搜索树，比较当前节点与前一个节点是否相等
        关键是如何保存相同个数的元素.
        """
        # # 方法1
        # self.table = defaultdict(int)
        #
        # def preOrder(root):
        #     if not root:
        #         return
        #     self.table[root.val] += 1
        #     preOrder(root.left)
        #     preOrder(root.right)
        #
        # preOrder(root)
        # nums = sorted(self.table.items(), key=lambda x: x[-1], reverse=True)
        # result = []
        # for i in range(len(nums)):
        #     if nums[i][1] == nums[0][1]:
        #         result.append(nums[i][0])
        #     else:
        #         break
        # return result

        # 方法2
        if not root:
            return []
        self.result = []
        self.maxCnt = 1
        self.curCnt = 1
        self.pre = None

        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            if self.pre:
                if root.val == self.pre.val:
                    self.curCnt += 1
                else:
                    self.curCnt = 1
                if self.curCnt > self.maxCnt:
                    self.maxCnt = self.curCnt
                    self.result = [root.val]
                elif self.curCnt == self.maxCnt:
                    self.result.append(root.val)
            else:
                self.result.append(root.val)
            self.pre = root
            inOrder(root.right)

        inOrder(root)
        return self.result

