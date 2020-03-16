class Solution:
    def reverse(self, x: int) -> int:
        # 1. 转换为字符串，反转后再转换成整数
        Minus = False
        if x < 0:
            Minus = True
            x = -x
        # reversed可以直接对字符串操作
        # sx = ''.join(list(reversed(str(x))))
        # sx = str(x)[::-1] 这两种反转操作时间效率差不多
        sx = str(x)[::-1]
        sx = int(sx)
        if sx >= 2 ** 31:  # 判断溢出
            return 0
        if Minus:
            sx = -sx

        return sx

        # 2. 手撕反转算法