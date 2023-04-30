class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """前K个高频元素
        1. 最小堆
        先统计词频, 转化为求前k大元素问题

        2. 快排
        """
        # # 1.
        # from collections import defaultdict
        # import heapq

        # counter = defaultdict(int)
        # arr = []
        # heapq.heapify(arr)
        # for num in nums:
        #     counter[num] += 1
        # for key, val in counter.items():
        #     if len(arr) < k:
        #         heapq.heappush(arr, (val, key))
        #     elif val > arr[0][0]:
        #         heapq.heappop(arr)
        #         heapq.heappush(arr, (val, key))
        # ans = [x[1] for x in arr]
        # return ans


        # 2.
        from collections import defaultdict
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        arr = list(counter.items())
        print(arr)

        def partition(left, right):
            pivot = arr[left]
            le = left
            for i in range(left+1, right+1):
                if arr[i][1] <= pivot[1]:
                    le += 1
                    arr[le], arr[i] = arr[i], arr[le]
            arr[le], arr[left] = arr[left], arr[le]
            return le

        l, r = 0, len(arr)-1
        target = len(arr)-k
        while l <= r:
            index = partition(l, r)
            if index == target:
                return [arr[i][0] for i in range(index, len(arr))]
            elif index < target:
                l = index + 1
            else:
                r = index - 1