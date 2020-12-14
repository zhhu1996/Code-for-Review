class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """串联字符串的最大长度
        1. 回溯法求组合问题，求出所有组合后依次判断组合是否满足条件

        2. 维护一个集合，当前回溯的时候就进行剪枝
        """
        # # 方法1
        # self.maxLen = 0
        #
        # def isUnique(string):
        #     if not string:
        #         return True
        #     s = set(string)
        #     if len(s) == len(string):
        #         return True
        #     else:
        #         return False
        #
        # def getCandidate(arr, index, s):
        #     if isUnique(s):
        #         self.maxLen = max(self.maxLen, len(s))
        #     for j in range(index, len(arr)):
        #         getCandidate(arr, j+1, s+arr[j])
        #
        # getCandidate(arr, 0, "")
        # return self.maxLen

        # 方法2
        self.maxLen = 0

        def getCandidate(arr, index, s, cur):
            for j in range(index, len(arr)):
                nowSet = set(arr[j])
                if len(nowSet) == len(arr[j]) and nowSet & cur == set():
                    self.maxLen = max(self.maxLen, len(cur | nowSet))
                    getCandidate(arr, j+1, s+arr[j], cur | nowSet)
                else:
                    getCandidate(arr, j+1, s, cur)

        getCandidate(arr, 0, "", set())
        return self.maxLen


