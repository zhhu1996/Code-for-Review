class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # # 1. step1: 生成全排列, step2: KMP算法匹配位置, 超时...
        # self.res = []
        # check = [0]*len(words)

        # def gen_substring(words, cur, check, index):
        #     if index >= len(words):
        #         self.res.append(cur)
        #         return
        #     for i in range(len(words)):
        #         if check[i]:
        #             continue
        #         check[i] = 1
        #         gen_substring(words, cur+words[i], check, index+1)
        #         check[i] = 0

        # def find_str(s, p):
        #     # KMP
        #     if not s:
        #         return -1
        #     # 1. 生成next数组
        #     next = [-1]
        #     i, j = 0, -1
        #     while i < len(p):
        #         if j == -1 or p[i] == p[j]:
        #             i += 1
        #             j += 1
        #             next.append(j)
        #         else:
        #             j = next[j]
            
        #     # 2. 根据next数组去匹配
        #     i, j = 0, 0
        #     while i < len(s) and j < len(p):
        #         if j == -1 or s[i] == p[j]:
        #             i += 1
        #             j += 1
        #         else:
        #             j = next[j]
        #     if j == len(p):
        #         return i-j
        #     return -1  

        # def find_all_str(s, p):
        #     # 暴力匹配
        #     res = []
        #     for i in range(len(s)):
        #         if p == s[i:(i+len(p))]:
        #             res.append(i)
        #     return res

        # gen_substring(words, '', check, 0)
        # ans = []
        # for p in self.res:
        #     k = find_str(s, p)
        #     pos = 0
        #     while k>=0:
        #         ans.append(pos+k)
        #         pos += k+1
        #         k = find_str(s[pos:], p)
                
        # return list(set(ans))

        # 2. 遍历字符串s的子串, 与words进行匹配, 匹配使用两个map, key存单词, value存单词出现次数
        from collections import defaultdict
        wordcnt = len(words)
        res = []
        if wordcnt <= 0:
            return []
        wordlen = len(words[0])
        # map1存储words的频次
        map1 = defaultdict(int)
        for w in words:
            map1[w] += 1
        for i in range(len(s)-wordcnt*wordlen+1):
            # map2存储子串的频次
            ts = s[i: i+wordcnt*wordlen]
            map2 = defaultdict(int)
            for j in range(wordcnt):
                sw = ts[j*wordlen: (j+1)*wordlen]
                map2[sw] += 1
            # map1, map2进行匹配
            contnum = 0
            for k,v in map2.items():
                if k not in map1.keys():
                    break
                if v > map1[k]:
                    break
                else:
                    contnum += 1
            # 匹配成功
            if contnum == len(map2):
                res.append(i)
        return res