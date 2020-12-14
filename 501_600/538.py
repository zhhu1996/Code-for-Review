# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """把二叉搜索树转换为累加树
        1. 中序遍历得到升序序列，对于第i个个元素，取[i+1: len]的和， 遍历了两次树的所有节点，时间复杂度高

        2. 在遍历当前节点之前，将所有大于该节点的值全部遍历完，并记录累加和
        即中序遍历反过来: 先遍历右子树、再根节点、再左子树

        3. 方法2的迭代形式
        """
        # # 方法1
        # self.array = []
        #
        # def inOrder(root):
        #     if not root:
        #         return
        #     inOrder(root.left)
        #     self.array.append(root.val)
        #     inOrder(root.right)
        #
        # inOrder(root)
        # localSum = 0
        # table = {}
        # n = len(self.array)
        # for i in range(n - 1, -1, -1):
        #     localSum += self.array[i]
        #     table[self.array[i]] = localSum
        #
        # def convert(root, table):
        #     if not root:
        #         return None
        #     root.val = table[root.val]
        #     root.left = convert(root.left, table)
        #     root.right = convert(root.right, table)
        #     return root
        #
        # return convert(root, table)

        # # 方法2
        # self.totalSum = 0
        #
        # def convertV2(root):
        #     if not root:
        #         return
        #     convertV2(root.right)
        #     self.totalSum += root.val
        #     root.val = self.totalSum
        #     convertV2(root.left)
        #
        # convertV2(root)
        # return self.totalSum

        # 方法3
        if not root:
            return None
        stack = []
        node = root
        totalSum = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            totalSum += node.val
            node.val = totalSum
            node = node.left
        return root
