class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """分割回文串
        1. 递归
        对于当前的索引index，目前已生成的回文字符串为cur，函数表示为dfs(s, index, cur)
        目的是找寻从index到len(s)的所有子串中，满足回文条件的子串，进行递归
        一旦不满足，进行回溯

        2. 动态规划
        以dp[i]表示以i结尾的字符串所包含的回文子串列表
        对于i
        dp[i] = dp[j] + s[j+1:i], 0<=j<=i-1
        此处+号代表列表中的append操作
        """
        def isSym(string):
            if not string:
                return True
            return string == string[::-1]

        # # 方法1
        # self.result = []
        #
        # def dfs(s, index, cur):
        #     if index == len(s):
        #         self.result.append(cur.copy())
        #         return
        #     for j in range(index, len(s)):
        #         if isSym(s[index: j + 1]):
        #             cur.append(s[index: j + 1])
        #             dfs(s, j + 1, cur)
        #             cur.pop()
        #
        # dfs(s, 0, [])
        # return self.result

        # 方法2
        if not s:
            return []
        dp = [[[s[0]]]]
        for i in range(1,len(s)):
            tmp = []
            for j in range(i,-1,-1):
                if isSym(s[j:i+1]):
                    if j == 0:
                        tmp.append([s[j:i+1]])
                        break
                    for k in range(len(dp[j-1])):
                        data = dp[j-1][k].copy()
                        data.append(s[j:i+1])
                        tmp.append(data)
            dp.append(tmp)
        return dp[-1]



