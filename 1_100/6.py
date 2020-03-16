class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #         # 1. 最慢的。。。，建了一个二维数组，将位置关系全部考虑了, 时间复杂度O(kn)，空间复杂度O(kn)
        #         n = len(s)
        #         if n == 0 or numRows == 0:
        #                 return ""
        #         if numRows == 1:
        #                 return s

        #         cnt = n // (2*numRows -2)
        #         tmp = n % (2*numRows - 2)
        #         rows = numRows
        #         cols = (numRows - 1) * cnt + max(1, tmp - numRows + 1)
        #         matrix = [[0]*cols for i in range(rows)]
        #         i, j, flag = 0, 0, 0
        #         for k in range(n):
        #             if flag == 0:
        #                 matrix[i][j] = s[k]
        #                 if i == rows - 1:
        #                     flag = 1
        #                     i -= 1
        #                     j += 1
        #                 else:
        #                     i += 1

        #             else:
        #                 # print(i, j)
        #                 matrix[i][j] = s[k]
        #                 if i == 1:
        #                     flag = 0
        #                     i -= 1
        #                     j += 1
        #                 elif i == 0:
        #                     flag = 0
        #                     i += 1
        #                 else:
        #                     i -= 1
        #                     j += 1
        #         # print(matrix)
        #         res = ''
        #         for x in range(rows):
        #             for y in range(cols):
        #                 if matrix[x][y]:
        #                     res += matrix[x][y]

        #         return res

        # 2. 不用考虑位置关系，直接用字符串列表来存储，相较于方法1，时间复杂度O(n), 空间复杂度O(n), n = len(s)
        if numRows == 1:
            return s

        rows = min(numRows, len(s))
        tmp = [[] for i in range(rows)]
        offset = -1
        i = 0
        for c in s:
            tmp[i].append(c)
            if i == 0 or i == rows - 1:
                offset = -offset
            i += offset
        res = ""
        for x in tmp:
            res += ''.join(x)
        return res