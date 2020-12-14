class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        table = {"1": "1", "6":"9", "8":"8", "9":"6", "0":"0"}

        def isStrobo(num, start, end, table):
            if start > end:
                return True
            if num[start] not in table or num[end] not in table or table[num[start]] != num[end]:
                return False
            return isStrobo(num, start+1, end-1, table)

        return isStrobo(num, 0, len(num)-1, table)