class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """统计优美子数组
        1. 暴力法， 统计所有子串中的奇数数字，O(n2)

        2. 滑动窗口
        不断右移 right 指针来扩大滑动窗口，使其包含 k 个奇数；
        若当前滑动窗口包含了 k 个奇数，则如下「计算当前窗口的优美子数组个数」：

        统计第 1 个奇数左边的偶数个数 leftEvenCnt。 这 leftEvenCnt 个偶数都可以作为「优美子数组」的起点，因此起点的选择有 leftEvenCnt + 1 种（因为可以一个偶数都不取，因此别忘了 +1 喔）。
        统计第 k 个奇数右边的偶数个数 rightEvenCnt 。 这 rightEvenCnt 个偶数都可以作为「优美子数组」的终点，因此终点的选择有 rightEvenCnt + 1 种（因为可以一个偶数都不取，因此别忘了 +1 喔）。
        因此「优美子数组」左右起点的选择组合数为 (leftEvenCnt + 1) * (rightEvenCnt + 1)。
        """
        if not nums or k <= 0:
            return 0
        i, j, n = 0, 0, len(nums)
        oddCnt = 0
        result = 0
        while j < n:
            if nums[j] % 2 == 1:
                oddCnt += 1
            if oddCnt == k:
                temp = j
                rightEvens = 0
                while j + 1 < n and nums[j + 1] % 2 == 0:
                    rightEvens += 1
                    j += 1
                leftEvens = 0
                while i <= temp and nums[i] % 2 == 0:
                    leftEvens += 1
                    i += 1
                result += (1 + leftEvens) * (1 + rightEvens)
                i += 1
                oddCnt -= 1
            j += 1

        return result
