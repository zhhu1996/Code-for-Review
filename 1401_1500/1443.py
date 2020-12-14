class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """收集树上所有苹果的最少时间
        1. 构建一个孩子节点指向父节点的逆向图，对于每个包含苹果的节点，向上搜索直到根节点或者已经搜索过的节点，并记录路径的长度
        最后得到的路径乘2
        """
        self.result = 0
        self.visited = [False] * n

        reversedEdges = [-1] * n
        for edge in edges:
            reversedEdges[edge[1]] = edge[0]
        self.visited[0] = True

        def dfs(root):
            if not self.visited[root]:
                self.visited[root] = True
                self.result += 1
                dfs(reversedEdges[root])

        for i in range(n):
            if hasApple[i]:
                dfs(i)
        return self.result * 2

