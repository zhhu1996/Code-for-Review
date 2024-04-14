class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """有向无环图中一个节点的所有祖先
        1. 拓扑排序 + 集合, 时间复杂度O(n^2)
        以拓扑排序遍历每个节点, 使用set进行祖先节点的合并, 最后再排序
        """
        q = deque()
        indeg = [0]*n
        g = defaultdict(list)
        for e in edges:
            f, t = e
            g[f].append(t)
            indeg[t] += 1
        path = [set() for _ in range(n)]
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            for nt in g[cur]:
                path[nt].add(cur)
                path[nt] = path[nt] | path[cur]
                indeg[nt] -= 1
                if indeg[nt] == 0:
                    q.append(nt)
        ans = []
        for p in path:
            ans.append(sorted(list(p)))
        return ans