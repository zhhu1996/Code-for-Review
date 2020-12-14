class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        """字母大小写全排列
        1. 回溯法，每次回溯选择1个字符

        2. 迭代
        对于当前的索引index，如果是数字，就直接插入到当前结果中，比如["A", "a"], 当前的是"1"，那么更新结果为["A1","a1"]
        如果是字母，那么将结果复制，前一半元素，每个append小写字母，后一半元素，每个append大写字母
        """
        # 方法1
        # self.result = []
        #
        # def getCandidate(s, index, p):
        #     if len(s) == index:
        #         self.result.append("".join(p))
        #         return
        #     if s[index].isdigit():
        #         c = s[index]
        #         p.append(c)
        #         getCandidate(s, index + 1, p)
        #         p.pop()
        #     else:
        #         alpha = s[index].lower()
        #         for c in [alpha, alpha.upper()]:
        #             p.append(c)
        #             getCandidate(s, index+1, p)
        #             p.pop()
        #
        # getCandidate(S, 0, [])
        # return self.result

        # 方法2
        result = [[]]

        for c in S:
            n = len(result)
            if c.isalpha():
                result.extend(result[:])
                for i in range(n):
                    result[i].append(c.lower())
                    result[i+n].append(c.upper())
            else:
                for i in range(n):
                    result[i].append(c)

        return map("".join, self.result)