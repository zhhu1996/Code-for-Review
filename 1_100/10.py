class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        s[0,i]表示从0到i的子串,p[0,j]表示从0到j的子串,若s[0,i]与p[0,j]匹配,则dp[i][j] = 1
        (1) s[i] = p[j] || p[j] = '.'
            => dp[i][j] = dp[i-1][j-1]
        (2) p[j] = '*'
            1)  s[i] == p[j-1] || p[j-1] == '.'
                i.  p[j-1]重复0次 
                => dp[i][j] = dp[i][j-2]
                ii. p[j-1]重复1次
                => dp[i][j] = dp[i-1][j-2]
                iii.p[j-1]重复>=2次, p的末尾仍是a*
                => dp[i][j] = dp[i-1][j]
            2) s[i] != p[j-1] && p[j-1] != '.'
               => dp[i][j] == dp[i][j-2]
        (3) p[j] != '*'
            => dp[i][j] = 0
        初始值:
        (1) s, p为空 
        => dp[0][0] = 1
        (2) s不空, p空
        => dp[j][0] = 0, j>=1
        (3) s空, p不空
            1) p[j] = '*'
            => dp[0][j] = dp[0][j-2]
            2) p[j] != '*'
            => dp[0][j] = 0
        """
        if not s and not p:
            return True 
        pn, sn = len(p), len(s)
        dp = [[False]*(pn+1) for i in range(sn+1)]
        dp[0][0] = True
        for i in range(1, pn+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        # dp
        for i in range(1, sn+1):
            for j in range(1, pn+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]              
                else:
                    dp[i][j] = False
        return dp[sn][pn]