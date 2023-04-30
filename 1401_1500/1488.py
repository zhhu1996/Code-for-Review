class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """避免洪水泛滥
        1. 二分
        使用哈希表记录已经装满水的琥珀以及日期, 在发生洪灾之前, 二分查找是否可以提前放水
        """
        ans = [1]*len(rains)
        records = {}
        reduce = []
        for i, val in enumerate(rains):
            if val > 0:
                ans[i] = -1
                if val in records:
                    # 首次>=target
                    target = records[val]
                    l, r = 0, len(reduce)-1
                    while l <= r:
                        mid = (l + r) // 2
                        if reduce[mid] < target:
                            l = mid + 1
                        else:
                            r = mid - 1
                    if l == len(reduce):
                        return []
                    # 治理湖泊
                    pos = reduce.pop(l)
                    ans[pos] = val 
                records[val] = i
            else:
                reduce.append(i)
        return ans