class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """分割回文串
        1. 递归
        对于当前的索引index，目前已生成的回文字符串为cur，函数表示为dfs(s, index, cur)
        目的是找寻从index到len(s)的所有子串中，满足回文条件的子串，进行递归
        一旦不满足，进行回溯
        """
        self.result = []

        def isSym(string):
            if not string:
                return True
            return string == string[::-1]

        def dfs(s, index, cur):
            if index == len(s):
                self.result.append(cur.copy())
                return
            for j in range(index, len(s)):
                if isSym(s[index: j + 1]):
                    cur.append(s[index: j + 1])
                    dfs(s, j + 1, cur)
                    cur.pop()

        dfs(s, 0, [])
        return self.result
