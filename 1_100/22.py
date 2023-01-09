class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #         # 1. 暴力法，到达最终状态的时候判断是否满足条件，如果是合法的括号组合则加入结果中, 时间复杂度O(2^2n * n)
        #         self.result = []
        #         self.generate("", 0, 2*n)
        #         return self.result

        #     def generate(self, array, index, length):
        #         if index == length:
        #             if self.validate(array):
        #                 self.result.append(array)
        #             return
        #         for c in ['(', ')']:
        #             self.generate(array+c, index+1, length)

        #     def validate(self, array):
        #         if not array:
        #             return True
        #         stack = []
        #         for c in array:
        #             if c == '(':
        #                 stack.append(c)
        #             elif c == ')' and stack and stack[-1] == '(':
        #                 stack.pop()
        #             else:
        #                 return False
        #         return not stack

        # # 2. 只需要保证右括号的数量一直小于当前左括号的数量，就一定满足条件
        # res = []

        # def getString(string, n, leftN, rightN):
        #     if len(string) == 2 * n:
        #         res.append(string)
        #         return

        #     if leftN < n:
        #         getString(string + '(', n, leftN + 1, rightN)

        #     if rightN < leftN:
        #         getString(string + ')', n, leftN, rightN + 1)

        # getString('', n, 0, 0)

        # return res

        # 3. 同解法2, 剪枝方法不同
        self.res = []

        def gen_cut_par(cur, index, maxlen, lcnt): 
            """
                cur: 当前生成的字符串
                index: 字符串长度
                maxlen: 最大长度, 即出口
                lcnt: 左括号的数量
            """
            if index == maxlen:
                if lcnt == maxlen//2: # 左括号数 = 右括号数, 才合法
                    self.res.append(cur)
                return
            if lcnt < index-lcnt: # 左括号数 < 右括号数
                return
            gen_cut_par(cur+'(', index+1, maxlen, lcnt+1)
            gen_cut_par(cur+')', index+1, maxlen, lcnt)

        gen_cut_par('', 0, 2*n, 0)
        return self.res 


