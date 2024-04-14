class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        """拼接数组的最大分数
        1. 辅助函数 + 最大区间和
        """
        # S1 = total1 - (presum1[right]-presum1[left]) + (presum2[right]-presum2[left])
        #    = total1 + (presum2[right]-presum1[right]) - (-presum1[left] + presum2[left])
        #    = total1 + y
        # S2 = total2 - (presum2[right]-presum2[left]) + (presum1[right]-presum1[left])
        #    = total2 + (presum2[left]-presum1[left]) - (presum2[right]-presum1[right])
        #    = total2 - y
        # ans = max(S1, S2)
        # y = (presum2[right]-presum1[right]) - (presum2[left]-presum1[left])
        # 辅助函数arr[i] = nums2[i] - nums1[i]
        # max: dpmx[i] = dpmx[i-1]>0, dpmx[i-1]+arr[i], arr[i]
        # min: dpmn[i] = dpmn[i-1]<0, dpmn[i-1]+arr[i], arr[i]

        assert len(nums1) == len(nums2)
        n = len(nums1)
        arr = [nums2[i]-nums1[i] for i in range(n)]
        dpmx, dpmn = [-float('inf')]*n, [float('inf')]*n
        for i in range(n):
            if i == 0:
                dpmx[i] = arr[i]
                dpmn[i] = arr[i]
            else:
                dpmx[i] = (max(dpmx[i], dpmx[i-1]+arr[i]) if dpmx[i-1] >= 0 else arr[i])
                dpmn[i] = (min(dpmn[i], dpmn[i-1]+arr[i]) if dpmn[i-1] <= 0 else arr[i])
        ymax, ymin = max(dpmx), min(dpmn)
        tsum1, tsum2 = sum(nums1), sum(nums2)
        return max(max(tsum1+ymax, tsum2-ymax), max(tsum1+ymin, tsum2-ymin))