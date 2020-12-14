class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        """将数组拆分成斐波那契数列
        1. 回溯法
        对于当前的索引index，如果result的元素个数小于3个，则直接添加；
        否则要判断当前的元素是否等于前两个元素之和
        """
        self.result = []

        def dfs(s, index, cur):
            if index == len(s):
                if len(cur) >= 3:
                    self.result = cur.copy()
                return
            for j in range(index, len(s)):
                if s[index] == "0" and j > index:
                    break
                number = int(s[index: j + 1])
                if len(cur) < 2 or (number == cur[-1] + cur[-2] and number <= 2**31-1):
                    cur.append(number)
                    dfs(s, j+1, cur)
                    cur.pop()

        dfs(S, 0, [])
        return self.result
