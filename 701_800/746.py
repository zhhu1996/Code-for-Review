class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """以最小花费爬楼梯
        dp: f[i] = min(f[i-1]+cost[i-1], f[i-2]+cost[i-2])
        """
        if not cost:
            return 0
        if len(cost) <= 2:
            return min(cost)
        f = [0, 0]
        for i in range(2, len(cost)+1):
            f.append(min(f[i-1]+cost[i-1], f[i-2]+cost[i-2]))
        return f[-1] 