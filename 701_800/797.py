class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """所有可能的路径
        1. dfs

        2. bfs
        """
        # 1.
        self.ans = []
        n = len(graph)
        visit = [False]*n

        def dfs(node, path):
            if node == n-1:
                path.append(node)
                self.ans.append(path.copy())
                path.pop()
                return
            visit[node] = True
            path.append(node)
            for i in graph[node]:
                if not visit[i]:
                    dfs(i, path)
            visit[node] = False
            path.pop()

        dfs(0, [])
        return self.ans