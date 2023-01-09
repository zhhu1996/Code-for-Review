class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # # 1. 滑动窗口, 用数组记录s与p中每个字符出现次数
        # if not s or not p or len(s) < len(p):
        #     return []
        # sl, pl = len(s), len(p)
        # arrs, arrp = [0]*26, [0]*26
        # res = []
        # for i in range(pl):
        #     arrs[ord(s[i])-ord('a')] += 1
        #     arrp[ord(p[i])-ord('a')] += 1
        # if arrs == arrp:
        #     res.append(0)
        # for i in range(sl-pl): # 窗口
        #     arrs[ord(s[i])-ord('a')] -= 1
        #     arrs[ord(s[i+pl])-ord('a')] += 1
        #     if arrs == arrp:
        #         res.append(i+1)
        # return res  

        # 2. 滑动窗口, 用数组记录s与p中不同字符的个数
        if not s or not p or len(s) < len(p):
            return []
        sl, pl = len(s), len(p)
        count = [0]*26
        res = []
        for i in range(pl):
            count[ord(s[i])-ord('a')] += 1
            count[ord(p[i])-ord('a')] -= 1
        diff = 0
        for num in count:
            if num != 0:
                diff += 1
        if diff == 0:
            res.append(0)
        for i in range(sl-pl):
            if count[ord(s[i])-ord('a')] == 1:
                diff -= 1
            elif count[ord(s[i])-ord('a')] == 0:
                diff += 1
            count[ord(s[i])-ord('a')] -= 1
            if count[ord(s[i+pl])-ord('a')] == -1:
                diff -= 1
            elif count[ord(s[i+pl])-ord('a')] == 0:
                diff += 1
            count[ord(s[i+pl])-ord('a')] += 1  
            if diff == 0:
                res.append(i+1)
        return res       
        
              