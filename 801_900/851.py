class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        """喧闹与富有
        1. dfs + 记忆化, 时间复杂度O(m+n), m=节点数, n=边数

        2. 拓扑排序, 时间复杂度O(m+n)
        以a->b建图, 进行拓扑排序
        """
        # # 1.
        # g = defaultdict(list)
        # cache = {}
        # for ai, bi in richer:
        #     g[bi].append(ai)
        
        # def dfs(start): # 返回从start出发的最小边
        #     if start in cache:
        #         return cache[start]
        #     val = quiet[start]
        #     index = start            
        #     visit[start] = True
        #     for end in g[start]:
        #         if not visit[end]:
        #             v, idx = dfs(end)
        #             if v < val:
        #                 val = v
        #                 index = idx
        #     visit[start] = False
        #     cache[start] = (val, index)
        #     return val, index

        # n = len(quiet)
        # visit = [False]*n
        # ans = []
        # for i in range(n):
        #     v, j = dfs(i)
        #     ans.append(j)
        # return ans


        # 2. 
        g = defaultdict(list)
        n = len(quiet)
        ins = [0]*n
        for ai, bi in richer:
            g[ai].append(bi)
            ins[bi] += 1
        # 入度为0的节点入队
        q = deque()
        ans = [i for i in range(n)]
        for i, d in enumerate(ins):
            if d == 0:
                q.append(i)
        # 拓扑排序
        while q:
            cur = q.popleft()
            for node in g[cur]:
                if quiet[ans[cur]] < quiet[ans[node]]:
                    ans[node] = ans[cur]
                ins[node] -= 1
                if ins[node] == 0:
                    q.append(node)
        return ans