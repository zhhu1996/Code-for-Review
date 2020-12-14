class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        """二进制手表
        1. 生成长度为10的、包含num个1的排列，再分别对时针和分针进行解析

        """
        self.result = []

        def parseTime(nums):
            base = 1
            result = 0
            for i in range(len(nums)):
                result += base * nums[i]
                base = base * 2
            return result

        def getCandidate(num, k, path):
            if len(path) == 10:
                if k == num:
                    hour, minute = parseTime(path[:4]), parseTime(path[4:])
                    if hour >= 0 and hour <= 11 and minute >= 0 and minute <= 59:
                        string = str(hour) + ":"
                        if minute <= 9:
                            string += "0"
                        string += str(minute)
                        self.result.append(string)
                return
            for i in range(2):
                path.append(i)
                if i == 1:
                    getCandidate(num, k+1, path)
                else:
                    getCandidate(num, k, path)
                path.pop()

        getCandidate(num, 0, [])
        return self.result
