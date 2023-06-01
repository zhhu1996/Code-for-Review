class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        """解码斜向换位密码
        1. 模拟
        根据encodedText模拟编码矩阵, 然后根据规则生成结果.注意最右边的空格需要删除
        空间优化: 可不生成矩阵, 直接遍历encodedText
        """
        # # 1.
        # lth = len(encodedText)
        # cols = lth // rows
        # ans = [[' ']*cols for _ in range(rows)]
        # for i, c in enumerate(encodedText):
        #     if c == ' ': continue
        #     ans[i//cols][i%cols] = c
        # encode = []
        # for i in range(cols):
        #     r, c = 0, i
        #     while r < rows and c < cols:
        #         encode.append(ans[r][c])
        #         r += 1
        #         c += 1
        # return ''.join(encode).rstrip()


        # 空间优化
        cols = len(encodedText) // rows
        encode = []
        for k in range(cols):
            r, c = 0, k
            while r < rows and c < cols:
                encode.append(encodedText[r*cols+c])
                r += 1
                c += 1
        return ''.join(encode).rstrip()