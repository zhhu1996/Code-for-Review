class Solution:
    def romanToInt(self, s: str) -> int:
        # 遇到每一个罗马数字，判断是否可能是出现在某个数字左边的情况（有6种）采取减法，其他都是加法
        dictData = {
            'I':             1,
            'V':             5,
            'X':             10,
            'L':             50,
            'C':             100,
            'D':             500,
            'M':             1000,
            'IV':            4,
            'IX':            9,
            'XL':            40,
            'XC':            90,
            'CD':            400,
            'CM':            900
        }
        cnt = 0
        length = len(s)
        for i in range(length):
            if s[i] in ['I', 'X', 'C'] and i+1 < length:
                # 考虑6种特殊情况
                if s[i] == 'I' and s[i+1] in ['V', 'X']:
                    cnt -= dictData[s[i]]
                elif s[i] == 'X' and s[i+1] in ['L', 'C']:
                    cnt -= dictData[s[i]]
                elif s[i] == 'C' and s[i+1] in ['D', 'M']:
                    cnt -= dictData[s[i]]
                else:
                    cnt += dictData[s[i]]
            else: # 其他情况直接加就行
                cnt += dictData[s[i]]
        return cnt