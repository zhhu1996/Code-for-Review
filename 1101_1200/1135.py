class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        """最低成本联通所有城市
        1. Kruskal算法 + 并查集
        每次取最小的边, 用并查集判断是否能构成更大的连通图
        优化1 -> 合并集合时总是将小集合合并到大集合中, find函数时间复杂度O(logn)
        优化2 -> 路径压缩: 将路径上所有节点的父节点置为根节点, find函数时间复杂度O(k)

        2. Prim算法 + 最小堆
        每次取集合中的顶点与集合外的顶点形成的最小边, 来生成更大的连通图
        """
        # 1.
        father = [i for i in range(n+1)]
        size = [1 for _ in range(n+1)]

        def find(x):
            if x == father[x]:
                return x
            father[x] = find(father[x])
            return father[x]

        connections.sort(key=lambda x: x[2])
        ans, edges = 0, 0
        for xi, yi, costi in connections:
            root_a = find(xi)
            root_b = find(yi)
            if root_a != root_b:
                if size[root_a] > size[root_b]:
                    root_a, root_b = root_b, root_a
                father[root_a] = root_b
                size[root_b] += size[root_a]
                ans += costi
                edges += 1
            if edges == n-1:
                return ans
        return -1


        # # 2.
        # edges = [[] for i in range(n + 1)] # 邻接表
        # for a, b, cost in connections:
        #     edges[a].append((b, cost))
        #     edges[b].append((a, cost))
        # intree = set()
        # out_edges = [(0, 1)] #（开销，目的城市）
        # ans = 0
        # while out_edges:
        #     cost, city = heapq.heappop(out_edges)
        #     if city not in intree:
        #         intree.add(city)
        #         ans += cost
        #         for next_city, next_cost in edges[city]:
        #             heapq.heappush(out_edges, (next_cost, next_city))
        # return ans if len(intree) == n else -1