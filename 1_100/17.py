class Solution:
    def __init__(self):
        self.result = []
        self.hashTable = None

    def letterCombinations(self, digits: str) -> List[str]:
        # # 1. 回溯法, 到达出口时统一存入结果
        # if not digits:
        #     return []
        # self.hashTable = {
        #     '2': 'abc',
        #     '3': 'def',
        #     '4': 'ghi',
        #     '5': 'jkl',
        #     '6': 'mno',
        #     '7': 'pqrs',
        #     '8': 'tuv',
        #     '9': 'wxyz'
        # }
        # self.sortStrings(digits, '', 0, len(digits))

        # return self.result

        # 2. 递归
        def gen_res(digits, cur, ss):
            """
            递归求解电话号码组合
                digits: 剩余需遍历的数组
                cur: 当前结果
                ss: 映射表
            """
            if not digits:
                return cur
            nc = ss[digits[0]]
            res = []
            if not cur:
                res = [c for c in nc]
            else:
                for s in cur:
                    for c in nc:
                        res.append(s+c)
            return gen_res(digits[1:], res, ss)

        return gen_res(digits, [], ss)

    def sortStrings(self, digits, s, index, maxLength):
        # 递归地对元素进行排列，s表示当前已经排列的字符
        # digits: 给定字符串
        # s: 生成的字符串
        # index: 当前索引
        # maxLength: 最大长度
        if index >= maxLength:
            self.result.append(s)
            return
        temp = self.hashTable[digits[index]]
        for c in temp:
            self.sortStrings(digits, s + c, index + 1, maxLength)
