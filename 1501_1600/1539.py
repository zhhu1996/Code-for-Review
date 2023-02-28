class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """第k个缺失的正整数
        1. 二分查找
        函数f[i] = arr[i] - (i+1), 表示位置i上缺失的正整数个数, 具备单调性
        寻找第一个i, f[i] >= k
        """
        l, r = 0, len(arr)-1
        while l <= r:
            # f(l-1) < k 
            # f(r+1) >= k
            mid = (l + r) // 2
            if arr[mid] - mid - 1 < k:
                l = mid + 1
            else:
                r = mid - 1
        # k - f(l-1) + arr[l-1]
        return k - (arr[l-1]-l) + arr[l-1]
        