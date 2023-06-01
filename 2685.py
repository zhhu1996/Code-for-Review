class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        """统计完全连通分量的数量
        1. dfs + 判断是否是完全联通分量, 时间复杂度O(m+n), m为边数, n为节点数
       遍历单个联通分量的同时计算节点个数以及边个数, e == v*(v-1)//2
        """
        g = defaultdict(list)
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        visit = [False]*n

        def dfs(cur):
            visit[cur] = True
            nonlocal v, e
            v += 1
            e += len(g[cur])
            for node in g[cur]:
                if not visit[node]:
                    dfs(node)

        ans = 0
        for i in range(n):
            if not visit[i]:
                v, e = 0, 0
                dfs(i)
                ans += (1 if e == v*(v-1) else 0)
        return ans