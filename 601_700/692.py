from collections import Counter
from heapq import *


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """前k个高频单词
        1. 计算出每个单词的出现次数，并对次数进行排序，时间O(nlogn)
        2. 维护一个有k个元素的最小堆，比较word的出现次数以及字母序来动态调整堆
        """
        # table = {}
        # for w in words:
        #     if w in table:
        #         table[w] += 1
        #     else:
        #         table[w] = 1
        # result = []
        # def compare(item1, item2):
        #     if item1[1] < item2[1]:
        #         return 1
        #     elif item1[1] > item2[1]:
        #         return -1
        #     elif item1[0] < item2[0]:
        #         return -1
        #     elif item1[0] > item2[0]:
        #         return 1
        #
        # from functools import cmp_to_key
        #
        # for key, value in sorted(table.items(), key=cmp_to_key(compare)):
        #     if len(result) < k:
        #         result.append(key)
        # return result

        counter = Counter(words)
        array = list(counter.items())

        def compare(node1, node2):
            """
            node1 > node2则返回Ture
            """
            if node1[1] > node2[1]:
                return True
            if node1[1] == node2[1] and node1[0] < node2[0]:
                return True
            return False

        # 手写最小堆
        def build(array, start, end):
            """
            调整start和end之间的子树使其形成最小堆的结构
            """
            while True:
                minChild = start * 2 + 1
                if minChild > end:  # 如果子节点大于最后一个节点，则终止
                    break
                if minChild + 1 <= end and compare(array[minChild], array[minChild + 1]):
                    minChild += 1
                if compare(array[start], array[minChild]):
                    array[start], array[minChild] = array[minChild], array[start]
                    start = minChild
                else:  # 如果当前节点小于子节点，则调整完毕
                    break

        def heapSort(array):
            """
            对array数组进行堆排序，堆的元素从0开始构建
            """
            if not array:
                return []

            n = len(array)
            firstRoot = n // 2 - 1
            for i in range(firstRoot, -1, -1):
                build(array, i, n - 1)
            for i in range(n - 1, 0, -1):
                array[i], array[0] = array[0], array[i]
                build(array, 0, i - 1)
            return array

        result = heapSort(array)
        print(result)
        return [result[i][0] for i in range(k)]



"""# 手写最小堆
def build(array, start, end):
    """
    #调整start和end之间的子树使其形成最小堆的结构
    """
    while True:
        minChild = start * 2 + 1
        if minChild > end: # 如果子节点大于最后一个节点，则终止
            break
        if minChild + 1 <= end and array[minChild] >= array[minChild+1]:
            minChild += 1
        if array[start] >= array[minChild]:
            array[start], array[minChild] = array[minChild], array[start]
            start = minChild
        else: # 如果当前节点小于子节点，则调整完毕
            break

def heapSort(array):
    """
    #对array数组进行堆排序，堆的元素从0开始构建
    """
    if not array:
        return []

    n = len(array)
    firstRoot = n // 2 -1
    for i in range(firstRoot, -1, -1):
        build(array, i, n-1)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        build(array, 0, i-1)

    return array

a = [1,3,5,7,9,2,4,6,8,0]
print(heapSort(a))"""