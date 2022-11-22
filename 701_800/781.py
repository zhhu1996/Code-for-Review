class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """兔子
        用map存储每个兔子的回答，遍历这个map，判断每种颜色的最少兔子数
        """
        from collections import defaultdict
        import math

        ans = defaultdict(int)
        for i in range(len(answers)):
            ans[answers[i]] += 1
        res = 0
        for k,v in ans.items():
            res += (k+1) * math.ceil(v / (k+1))
        return res