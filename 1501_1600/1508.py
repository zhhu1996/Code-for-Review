class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """子数组和排序后的区间和
        1. 模拟, 时间复杂度O(n*nlogn)

        2. 双指针 + 二分查找, 时间复杂度O(nlogn)
        f(k)表示前k大的区间和
        """
        psum = [0]*(n+1)
        ppsum = [0]*(n+1)
        for i in range(1, n+1):
            psum[i] = psum[i-1] + nums[i-1]
        for i in range(1, n+1):
            ppsum[i] = ppsum[i-1] + psum[i]

        def f(k): # 前k个元素的和
            x = get_kth_num(k)
            tsum, cnt = calc_sum_cnt(x)
            return tsum + (k-cnt)*x

        def calc_sum_cnt(x): # 双指针求小于x的和与个数
            j, tsum, cnt = 0, 0, 0
            for i in range(n):
                while j < n and psum[j+1]-psum[i] < x:
                    j += 1
                cnt += (j-i)
                # S_i,i + S_i,i+1 + ... + S_i,j-1
                tsum += (ppsum[j]-ppsum[i]) - (j-i)*psum[i]
            return (tsum, cnt)

        def get_kth_num(k): # 二分查找第k小的区间和
            l, r = min(nums), psum[-1]
            while l <= r:
                mid = (l + r) // 2
                # f(l-1)<k, f(l)>=k
                tsum, cnt = calc_sum_cnt(mid)
                if cnt < k:
                    l = mid + 1
                else:
                    r = mid - 1
            # f(l) >= k
            return l-1
        
        return (f(right) - f(left-1)) % (10**9 + 7)