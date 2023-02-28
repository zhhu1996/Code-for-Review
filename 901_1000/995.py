class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        """k连续位的最小翻转次数
        1. 暴力, 时间复杂度O(nk), 超时
        对于每一次反转, 只影响[i..i+k-1]的元素, [0..i-1]的元素不变
        => 对于每次出现的0, 至少需要1次反转才能变成1

        2. 滑动窗口
        i. nums[i] = 0 and [i-k+1..i-1]中反转的次数为偶数 => i也要反转
        ii.nums[i] = 1 and [i-k+1..i-1]中反转的次数为奇数 => i要反转
        => ([i-k+1..i-1]中反转的次数) % 2 == nums[i] 则需要反转
        可利用队列表示窗口
        元素入列: 当前位置需要反转
        元素出列: 队首元素<i-k+1
        """
        # 2.
        n = len(nums)
        q = collections.deque()
        res = 0
        for i in range(n):
            if q and q[0] < i-k+1:
                q.popleft()
            if len(q) % 2 == nums[i]:
                if i > n-k:
                    return -1
                q.append(i)
                res += 1
        return res
