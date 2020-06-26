class Solution:
    def hammingWeight(self, n: int) -> int:
        """位操作
        1. flag左移位
        2. n-1之后与n按位与，会把n最右边的1变成0
        """

        # flag = 1
        # cnt = 0
        # while n >= flag:
        #     if n & flag:
        #         cnt += 1
        #     flag = flag << 1
        # return cnt

        cnt = 0
        while n > 0:
            cnt += 1
            n = (n-1) & n
        return cnt