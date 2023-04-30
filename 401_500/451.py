class Solution:
    def frequencySort(self, s: str) -> str:
        """根据字符出现频率排序
        1. 统计词频后排序(快排/堆排序/桶排序)
        """
        from collections import defaultdict
        
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        ans = ''
        for k, v in sorted(counter.items(), key=lambda x: x[1], reverse=True):
            ans += k*v
        return ans