class Solution:
    def findContestMatch(self, n: int) -> str:
        """输出比赛匹配对"""
        def findMatch(now):
            if len(now) < 2:
                return now
            result = []
            for i in range(len(now)//2):
                s = "(" + str(now[i]) + "," + str(now[len(now)-1-i]) + ")"
                result.append(s)
            return findMatch(result)

        nums = [i for i in range(1,n+1)]
        return findMatch(nums)[0]
