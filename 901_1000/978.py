class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        """最大湍流子数组
        1. 滑动窗口法，如何维护窗口使其满足性质？
        湍流：(a[j]-a[j-1])*(a[j+1]-a[j]) < 0
        最大：满足湍流的条件下j++
             不满足的条件下i=j,j++
        """
        if not A:
            return 0
        n = len(A)
        i, j = 0, 1
        maxLen = 0
        while j < n:
            c = A[j] - A[j - 1]
            if j == n - 1 or c * (A[j + 1] - A[j]) >= 0:
                if c != 0:
                    maxLen = max(maxLen, j - i + 1)
                i = j
            j += 1
        return maxLen
