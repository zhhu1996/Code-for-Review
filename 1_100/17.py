class Solution:
    def __init__(self):
        self.result = []
        self.hashTable = None

    def letterCombinations(self, digits: str) -> List[str]:
        # 1. 回溯法，当到达规定状态时进行操作并返回上层调用
        if not digits:
            return []
        self.hashTable = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.sortStrings(digits, '', 0, len(digits))

        return self.result

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
