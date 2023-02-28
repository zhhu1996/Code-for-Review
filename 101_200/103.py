# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """二叉树的锯齿形层序遍历
        1. 层序遍历 + 队列

        2. 层序遍历 + 堆栈
        """
        # # 1. 
        # from queue import Queue
        # if not root: return []
        # q = Queue(-1)
        # q.put(root)
        # is_left = True
        # res = []
        # while not q.empty():
        #     level = []
        #     size = q.qsize()
        #     for i in range(size):
        #         node = q.get()
        #         if node.left:
        #             q.put(node.left)
        #         if node.right:
        #             q.put(node.right)
        #         level.append(node.val)
        #     if is_left:
        #         res.append(level.copy())
        #     else:
        #         res.append(level[::-1])
        #     is_left = not is_left
        # return res  

        # 2.
        if not root: return []
        s1, s2 = [root], []
        level, res = [], []
        while s1 or s2:
            level = []
            if s1: # 当层左->右, 下层右->左
                while s1: 
                    cur = s1.pop()
                    if cur.left:
                        s2.append(cur.left)
                    if cur.right:
                        s2.append(cur.right)
                    level.append(cur.val)
                res.append(level.copy())
            else: # 当层右->左， 下层左->右
                while s2: 
                    cur = s2.pop()
                    if cur.right:
                        s1.append(cur.right)
                    if cur.left:
                        s1.append(cur.left)
                    level.append(cur.val)
                res.append(level.copy())
        return res