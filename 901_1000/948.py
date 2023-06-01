class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """令牌放置
        1. 贪心 + 双指针
        左指针负责加得分, 右指针负责加能量
        """
        tokens.sort()
        i, j = 0, len(tokens)-1
        ans = 0
        res = 0
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                ans += 1
                i += 1
            elif ans > 0:
                power += tokens[j]
                ans -= 1
                j -= 1
            else:
                break
            res = max(res, ans)
        return res