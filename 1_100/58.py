class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 1. 手写
        s = s.strip()
        cnt = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                cnt += 1
            else:
                break
        return cnt

        # # 2. split
        # s = s.strip()
        # strArray = s.split(" ")
        # return len(strArray[-1])