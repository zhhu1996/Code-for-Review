class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        """可移除字符的最大数目
        1. 二分查找
        """
        def is_valid(x):
            rm_set = set(removable[:x])
            i, j = 0, 0
            while i < len(s) and j < len(p):
                if i in rm_set:
                    i += 1
                    continue
                if s[i] == p[j]:
                    j += 1
                i += 1
            return j == len(p)

        l, r = 0, len(removable)
        while l <= r:
            mid = (l + r) // 2
            if is_valid(mid):
                l = mid + 1
            else:
                r = mid - 1
        # f(l-1) = True
        return l-1