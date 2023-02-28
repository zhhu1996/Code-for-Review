class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """单词拆分
        1. 回溯生成可生成的所有排列, 超时
        2. dfs + 记忆化
        从s的第一位开始判断是否能够匹配
        3. bfs + 记忆化
        4. dp
        单串, 位置i必须取, O(n)个子问题
        dp[i]: s[0..i]是否可以由字典组成
        """
        # # 2.
        # self.wordset = set(wordDict)
        # self.mem = {} # 记忆化

        # def dfs(s, index):
        #     if index >= len(s):
        #         return True
        #     if index in self.mem:
        #         return self.mem[index]

        #     for i in range(index, len(s)):
        #         cur = s[index: i+1]
        #         if cur in self.wordset and dfs(s, i+1):
        #             self.mem[index] = True
        #             return True
            
        #     self.mem[index] = False
        #     return False
        
        # return dfs(s, 0)
        
        # 4.
        n = len(s)
        wordset = set(wordDict)
        dp = [False]*(1+n)
        dp[0] = True
        # i表示长度
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
        return dp[n]
        