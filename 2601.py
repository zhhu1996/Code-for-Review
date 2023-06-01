class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        """质数减法运算
        1. 贪心 + 二分
        每个元素在大于前一个元素的前提下尽可能的小, 这样能形成严格递增数组的概率最大
        """
        def gen_prime(target):
            """埃氏筛法"""
            mx = target + 1
            primes = []
            is_prime = [True] * mx
            for i in range(2, mx):
                if is_prime[i]:
                    primes.append(i)
                    for j in range(i*i, mx, i):
                        is_prime[j] = False
            return primes

        def binary_search(arr, target): # 搜索 <target 的最大值
            l, r = 0, len(arr)-1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return 0 if l == 0 else arr[l-1]
        
        cands = gen_prime(1000)
        for i in range(len(nums)):
            target = nums[i]
            if i == 0:
                nums[i] -= binary_search(cands, target) # 二分查找
            else:
                nums[i] -= binary_search(cands, target-nums[i-1])
                if nums[i] <= nums[i-1]:
                    return False
        return True