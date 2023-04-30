class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """字母异位词分组
        1. 哈希
        哈希函数的选择:
        1) sort, 时间复杂度O(klogk)
        2) 统计字母频次, 时间复杂度O(k+26)
        """
        ans_map = {}

        def calc_key(s):
            ans = ''
            chs = [0]*26
            for c in s:
                pos = ord(c) - ord('a')
                chs[pos] += 1
            for i in range(26):
                if chs[i] > 0:
                    ans += str(chs[i]) + '_' + chr(i+97) + ','
            return ans
        
        for s in strs:
            k = calc_key(s)
            if k in ans_map:
                ans_map[k].append(s)
            else:
                ans_map[k] = [s]
        return list(ans_map.values())