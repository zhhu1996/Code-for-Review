class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. 哈希存储，将字母异位词映射到同一位置， 时间复杂度: O(N*K*logK)
        # dicts = {}
        # for string in strs:
        #     temp = ''.join(sorted(string))
        #     if temp in dicts:
        #         dicts[temp].append(string)
        #     else:
        #         dicts[temp] = [string]
        # return list(dicts.values())

        # 2. 按照字母计数分类
        dicts = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            if tuple(key) in dicts:
                dicts[tuple(key)].append(s)
            else:
                dicts[tuple(key)] = [s]
        return list(dicts.values())


