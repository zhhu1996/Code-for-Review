class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        """树的直径
        1. 两次搜索, 时间复杂度O(n)
        从任意一点a开始, 距离最远的端点必定是直径的端点之一b(https://leetcode.cn/problems/tree-diameter/solutions/1/wei-shi-yao-ke-yi-liang-ci-by-aw2434-a6y1/); 从b出发搜索最远的点c必定是另一个端点
        """  
        g = defaultdict(list)
        start = 0
        for e in edges:
            f, t = e
            g[f].append(t)
            g[t].append(f)
            start = f

        def bfs(start):
            q = deque()
            visit = set()
            res = start
            cur = 0
            q.append(start)
            visit.add(start)
            while q:
                qsize = len(q)
                for i in range(qsize):
                    node = q.popleft()
                    res = node
                    for nxt in g[node]:
                        if nxt not in visit:
                            q.append(nxt)
                            visit.add(nxt)
                cur += 1
            return res, cur-1

        b, _ = bfs(start)
        c, ans = bfs(b)
        return ans