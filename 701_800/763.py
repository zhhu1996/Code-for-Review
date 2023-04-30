class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """划分字母区间
        1. 贪心 + 双指针, 时间复杂度O(n)
        遍历字符串, 记录每个字符串出现的最大位置. 通过双指针记录生成的片段
        """
        pos_map = defaultdict(int)
        for i, c in enumerate(s):
            pos_map[c] = i
        i, j = 0, pos_map[s[0]]
        ans = []
        cumsum = 0
        while i < len(s):
            j = max(pos_map[s[i]], j)
            if i == j:
                if not ans:
                    ans.append(j+1)
                    cumsum += j+1
                else:
                    ans.append(j+1-cumsum)
                    cumsum += ans[-1]
            i += 1
        return ans