class Solution:
    def numDecodings(self, s: str) -> int:
        # f[n]代表到第n个字符串时具有的解码方法总数
        # f[n] = f[n-1]+ f[n-2],    if 0 < s[n-1: n+1] <= 26 and s[n-1] and s[n]
        # f[n] = f[n-2],            if 0 < s[n-1: n+1] <= 26 and s[n] == '0'
        # f[n] = f[n-1],            if s[n-1: n+1] > 26 and s[n] != '0'
        # 0，                        else
        n = len(s)
        if s[0] == '0':
            return 0

        if n == 1:
            return 1

        # 前2位字符的解码数
        f = [0] * n
        f[0] = 1
        if int(s[:2]) <= 26:
            if s[1] != '0':
                f[1] = 2
            else:
                f[1] = 1
        else:
            if s[1] != '0':
                f[1] = 1
            else:
                return 0

        for i in range(2, n):
            if int(s[i - 1: i + 1]) <= 26 and int(s[i - 1: i + 1]) > 0:
                if s[i - 1] != '0' and s[i] != '0':
                    f[i] = f[i - 1] + f[i - 2]
                elif s[i] == '0' and s[i - 1] != '0':
                    f[i] = f[i - 2]
                elif s[i - 1] == '0' and s[i] != '0':
                    f[i] = f[i - 1]
                else:
                    return 0
            elif int(s[i - 1: i + 1]) > 26:
                if s[i] != '0':
                    f[i] = f[i - 1]
                else:
                    return 0
            else:  # < 0
                return 0

        return f[n - 1]