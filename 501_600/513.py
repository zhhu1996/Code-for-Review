# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """找树左下角的值
        1. BFS

        2. DFS
        """
        # # 1.  
        # from queue import Queue
        # q = Queue(-1)
        # q.put(root)
        # p = None
        # while not q.empty():
        #     size = q.qsize()
        #     for i in range(size):
        #         cur = q.get()
        #         if i == 0:
        #             p = cur
        #         if cur.left:
        #             q.put(cur.left)
        #         if cur.right:
        #             q.put(cur.right)
        # return p.val

        # 2.  
        self.depth = 0
        self.res = root

        def dfs(root, depth):
            if not root: return
            if self.depth < depth:
                self.depth = depth
                self.res = root
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)

        dfs(root, 0)
        return self.res.val