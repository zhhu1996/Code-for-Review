class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        """摧毁一系列目标
        1. 取模, 时间复杂度O(n)
        等差数列中的所有元素对差取模后是相等的
        """
        # 1.
        mods = defaultdict(list)
        for num in nums:
            mods[num % space].append(num)
        maxl, ans = 0, 0
        for v in mods.values():
            l, x = len(v), min(v)
            if maxl < l or (maxl == l and ans > x):
                maxl, ans = l, x
        return ans