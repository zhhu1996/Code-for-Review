class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """分割回文串
        1. 动态规划
        以dp[i]表示以i结尾的字符串所包含的回文子串最小分割次数
        对于i
        dp[i] = min(dp[i], dp[j] + 1), 0<=j<=i-1 if s[j+1:i] is 回文
        此处+号代表列表中的append操作
        """
        def isSym(string):
            if not string:
                return True
            return string == string[::-1]

        # 方法2
        if not s:
            return []
        dp = [0]
        for i in range(1,len(s)):
            tmp = float("inf")
            for j in range(i,-1,-1):
                if isSym(s[j:i+1]):
                    tmp = min(tmp, dp[j]+1)
            dp.append(tmp)
        return dp[-1]



