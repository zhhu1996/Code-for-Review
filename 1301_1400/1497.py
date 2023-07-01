class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        """检查数组对是否可以被 k 整除
        1. 哈希表, 时间复杂度O(n)
        只需要找到(a + b) % k = 0即可
        """
        counter = defaultdict(int)
        pairs = 0
        for num in arr:
            cur = num % k
            if counter[(k-cur)%k] > 0:
                counter[(k-cur)%k] -= 1
                pairs += 1
            else:
                counter[cur] += 1
        return pairs == len(arr)//2