class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """移位字符串分组
        1. 哈希表
        key: 遍历字符串, 将与首字符的diff连接起来作为key
        """
        n = len(strings)
        maps = {}
        res = []
        for i in range(n):
            s = strings[i]
            diffs = []
            for j in range(len(s)):
                diff = (ord(s[j]) - ord(s[0]) + 26) % 26
                diffs.append(str(diff))
            key = '_'.join(diffs)
            if key in maps:
                maps[key].append(s)
            else:
                maps[key] = [s]
        for k, v in maps.items():
            res.append(v)
        return res            
