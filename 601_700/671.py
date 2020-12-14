# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        """二叉树中的第二小节点
        每个节点的值定义为
        如果是叶子节点，则是自身的值；
        如果有两个孩子节点，则是孩子节点中较小的一个

        1. 层序遍历，将每个节点的值存入列表(也可使用集合)中，对列表查询第二小的值，O(n)

        2. 根据定义，根节点一定是值最小的节点。那么第二小的节点就是找到比根节点大的最小节点即可


        """
        # # 方法1
        # if not root:
        #     return -1
        # queue = Queue(1000)
        # queue.put(root)
        # result = []
        # while not queue.empty():
        #     node = queue.get()
        #     if node.left and node.right:
        #         result.append(min(node.left.val, node.right.val))
        #     elif not node.left and not node.right:
        #         result.append(node.val)
        #     if node.left:
        #         queue.put(node.left)
        #     if node.right:
        #         queue.put(node.right)
        # first, second = float("inf"), float("inf")
        # for i in range(len(result)):
        #     if result[i] < first:
        #         first = result[i]
        #         second = first
        #     elif result[i] < second:
        #         second = result[i]
        # if first == second:
        #     return -1
        # else:
        #     return second

        # 方法2
        def search(root, target):
            if not root:
                return -1
            if root.val > target:
                return root.val
            l = search(root.left, target)
            r = search(root.right, target)
            if l == -1:
                return r
            if r == -1:
                return l
            return min(l, r)

        return search(root, root.val)





