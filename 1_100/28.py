class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # # 1. Python自带的查询字符串位置的函数
        # if not needle:
        #     return 0
        # try:
        #     res = haystack.index(needle)
        # except:
        #     res = -1
        # return res

        # # 2. bf
        # if not needle:
        #     return 0
        # for i in range(len(haystack)):
        #     if haystack[i: i+len(needle)] == needle:
        #         return i
        # return -1

        # # 3. kmp
        # # 计算next数组
        # next = [-1]
        # i, j = 0, -1
        # while i < len(needle):
        #     if j == -1 or needle[i] == needle[j]:
        #         i += 1
        #         j += 1
        #         next.append(j)
        #     else:
        #         j = next[j]
        #
        # # kmp
        # i, j = 0, 0
        # while i < len(haystack) and j < len(needle):
        #     if j == -1 or haystack[i] == needle[j]:
        #         i += 1
        #         j += 1
        #     else:
        #         j = next[j]
        # if j == len(needle):
        #     return i - j
        # return -1

        # # 4. 双指针，方法2的优化，不需要完全判断，当某个字符不同即可停止判断

        # 5. Sunday算法
        pset = set(needle)
        table = {}
        for c in pset:
            j = len(needle)-1
            while j >= 0:
                if needle[j] == c:
                    table[c] = len(needle) - j
                    break
                j -= 1
        table["other"] = len(needle) + 1

        i = 0
        while i < len(haystack)-len(needle)+1:
            flag = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    flag = False
                    break
            if flag:
                return i
            else:
                if i + len(needle) < len(haystack):
                    nextc = haystack[i+len(needle)]
                    if nextc in table:
                        i += table[nextc]
                    else:
                        i += table["other"]
                else:
                    break
        return -1



