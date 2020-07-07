from heapq import *

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """找到最小的k个数
        1. partition方法：时间复杂度O(n)，找到的k个数并非是有序的，会修改原数组，因为要把数组全部读入内存，所以不适用于海量数据

        2. 最大堆：建立一个可存储k个元素的最大堆，遍历数组，对于每个元素，需要做查找，插入，删除操作，时间复杂度O(nlogk)
                  不需要修改数组，适用于海量数据
        """

        # 方法1
        def partition(array, length, start, end):
            if start < 0 or end >= length:
                return None
            index = start - 1
            point = start
            while point < end:
                if array[point] < array[end]:
                    index += 1
                    array[index], array[point] = array[point], array[index]
                point += 1
            index += 1
            array[index], array[end] = array[end], array[index]
            return index

        # if k <= 0:
        #     return []
        # if k >= len(arr):
        #     return arr
        # start, end = 0, len(arr)-1
        # index = partition(arr, len(arr), start, end)
        # while index != k-1:
        #     if index > k-1:
        #         end = index-1
        #         index = partition(arr, len(arr), start, end)
        #     else:
        #         start = index+1
        #         index = partition(arr, len(arr), start, end)
        # return arr[:k]

        # 方法2
        if k <= 0:
            return []
        if k >= len(arr):
            return arr
        bigHeap = []
        for i in range(len(arr)):
            if i < k:
                heappush(bigHeap, (-arr[i], arr[i]))
            elif i >= k and bigHeap[0][1] > arr[i]:
                heappop(bigHeap)
                heappush(bigHeap, (-arr[i], arr[i]))
        res = []
        for x in bigHeap:
            res.append(x[1])
        return res

