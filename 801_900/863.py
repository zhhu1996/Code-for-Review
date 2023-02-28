# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """二叉树中所有距离为k的节点
        1. 先dfs建立无向图, 再bfs寻找与目标节点距离为k的节点
        """
        # 1.
        from queue import Queue

        self.graph = {}
        self.visit = set() # 相较于二叉树的bfs, 新增了访问位置判断
        
        def add(i, j):
            if i in self.graph:
                self.graph[i].append(j)
            else:
                self.graph[i] = [j]
        
        def dfs(root):
            if not root:
                return
            if root.left:
                add(root.left.val, root.val)
                add(root.val, root.left.val)
                dfs(root.left)
            if root.right:
                add(root.right.val, root.val)
                add(root.val, root.right.val)
                dfs(root.right)
        
        dfs(root)
        start = target.val
        q = Queue(-1)
        q.put(start)
        while not q.empty() and k > 0:
            qsize = q.qsize()
            for i in range(qsize):
                cur = q.get()
                self.visit.add(cur)
                if cur in self.graph:
                    neighbours = self.graph[cur]
                    for nb in neighbours:
                        if nb not in self.visit: # 防止重复遍历
                            q.put(nb)
            k -= 1
        res = []
        while not q.empty():
            res.append(q.get())
        return res