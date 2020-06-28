class Solution:
    def isNumber(self, s: str) -> bool:
        """A.BeC
        A,C都是有符号整数，B是无符号整数
        1. 首先判断是否有非法字母
        2. 切分A,B,C
        3. 判断逻辑：
            i. 存在小数点: A or B
            ii. 存在e: flag and C
            iii. 最后需要再判断一次B，因此B或操作会遗漏一种情况
        """
        s = [c.lower() for c in s.strip()]
        pointCnt, eCnt = 0, 0
        pointIndex, eIndex = -1, -1
        validFlag = False
        allowStr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.', 'e']
        for i in range(len(s)):
            if s[i] == '.':
                pointCnt += 1
                pointIndex = i
            if s[i] == 'e':
                eCnt += 1
                eIndex = i
            if s[i] not in allowStr:
                validFlag = True
                break
        if pointCnt > 1 or eCnt > 1 or validFlag:
            return False
        if pointIndex > -1 and eIndex > -1:
            A, B, C = s[: pointIndex], s[pointIndex + 1: eIndex], s[eIndex + 1:]
        elif pointIndex > -1:
            A, B, C = s[: pointIndex], s[pointIndex + 1:], []
        elif eIndex > -1:
            A, B, C = s[: eIndex], [], s[eIndex + 1:]
        else:
            A, B, C = s, [], []

        def isUnsignedNumber(array):
            if not array:
                return False
            allowNum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            for x in array:
                if x not in allowNum:
                    return False
            return True

        def isSignedNumber(array):
            if not array:
                return False
            if array[0] in '+-':
                return isUnsignedNumber(array[1:])
            else:
                return isUnsignedNumber(array)

        flag = False
        if A:
            flag = isSignedNumber(A)
        if pointIndex > -1:
            flag = flag or isUnsignedNumber(B)
        if eIndex > -1:
            flag = flag and isSignedNumber(C)
        if B:
            flag = flag and isUnsignedNumber(B)
        return flag
