class Solution:
    def nextClosestTime(self, time: str) -> str:
        """最近时刻
        1. 通过回溯法求到所有的候选时刻，然后逐个比较距离，选则最小的。注意，当"00:00"、"11:11"这样的输入，返回原始值
        """

        def calcDistance(time1, time2):
            # time1是初始字符串，time2是候选字符串
            m1 = int(time1[:2]) * 60 + int(time1[-2:])
            m2 = int(time2[:2]) * 60 + int(time2[-2:])
            return (m2 - m1) % 1440

        def isValid(timeList):
            timeString = "".join(timeList)
            if int(timeString[:2]) >= 24:
                return False
            if int(timeString[-2:]) >= 60:
                return False
            return True

        def isEqual(time):
            # "0000", "1111"
            for i in range(1, len(time)):
                if time[i] != time[i - 1]:
                    return False
            return True

        self.result = []

        def getCandidate(array, index, now):
            if index == len(array):
                self.result.append("".join(now.copy()))
                return
            for i in range(len(array)):
                now.append(array[i])
                getCandidate(array, index + 1, now)
                now.pop()

        if isEqual(time[:2] + time[3:]):
            return time
        timeList = list(time)
        minDist, minTime = float("inf"), None
        getCandidate(time[:2] + time[3:], 0, [])
        for s in self.result:
            dist = calcDistance(time[:2] + time[3:], s)
            # print(s, dist)
            if isValid(s) and dist > 0 and minDist > dist:
                minDist = dist
                minTime = s
        # print(minDist, minTime)
        return minTime[:2] + ":" + minTime[2:]