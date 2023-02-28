class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        1. 维护一个长度为k的最小堆, 堆顶元素即为第k大

        2. 双指针+快速排序
        循环不变体: 取left位置的元素作为基准pivot, [left+1..le]均小于pivot
        """
        # # 1.
        # import heapq
        # topk = []
        # heapq.heapify(topk)
        # for i in range(len(nums)):
        #     if len(topk) < k:
        #         heapq.heappush(topk, nums[i])
        #     elif topk[0] < nums[i]:
        #         heapq.heappop(topk)
        #         heapq.heappush(topk, nums[i])
        # return heapq.heappop(topk)

        # 2.
        n = len(nums)
        target = n - k

        def do_partition(nums, left, right):
            pivot = nums[left]
            le = left
            for i in range(left+1, right+1):
                if nums[i] <= pivot:
                    le += 1
                    nums[le], nums[i] = nums[i], nums[le]
            nums[left], nums[le] = nums[le], nums[left]
            return le

        left, right = 0, n-1
        while True:
            index = do_partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                left = index + 1
            else:
                right = index - 1