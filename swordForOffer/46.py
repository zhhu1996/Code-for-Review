class Solution:
    def translateNum(self, num: int) -> int:
        """把数字翻译成字符串
        if 10 <= s[i-1: i+1] <= 25:  f[i] = f[i-1] + f[i-2]
        else:  f[i] = f[i-1]
        """
        nums = str(num)
        n = len(nums)
        f = []
        if 10 <= int(nums[:2]) <= 25:
            f.extend([1, 2])
        else:
            f.extend([1, 1])
        for i in range(2, n):
            if 10 <= int(nums[i-1: i+1]) <= 25:
                f.append(f[i-2] + f[i-1])
            else:
                f.append(f[i-1])
        return f[-1]