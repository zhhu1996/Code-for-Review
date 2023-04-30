class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """可以到达所有点的最少点数目
        1. 有向图
        寻找入度为0的节点
        """
        degree = [[0,0] for _ in range(n)] # [入度, 出度]
        ans = []
        for e in edges:
            s, e = e[0], e[1]
            degree[s][1] += 1
            degree[e][0] += 1
        for i in range(n):
            if degree[i][0] == 0:
                ans.append(i)
        return ans