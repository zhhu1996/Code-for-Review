class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """找到小镇的法官
        1. 图, 时间复杂度O(n)
        在有向图中搜索一个节点, 其入度为n, 出度为0
        """
        degree = [[0,0] for _ in range(n+1)] # [入度, 出度]
        for t in trust:
            ai, bi = t[0], t[1]
            degree[ai][1] += 1
            degree[bi][0] += 1
        for i in range(1, n+1):
            if degree[i][0] == n-1 and degree[i][1] == 0:
                return i
        return -1      