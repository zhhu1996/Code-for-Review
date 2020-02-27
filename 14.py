class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # # 1. lcp(s1,s2,...,sn) = lcp(lcp(s1,s2), ..., sn), 时间O(s)，s是所有字符的数量

        # # 2. 水平扫描法，直接找到最短字符串的长度，然后逐个比较，时间O(s)，会比方法1快点
        # if not strs:
        #     return ""
        # if len(strs) == 1:
        #     return strs[0]
        # minl = min([len(x) for x in strs])
        # end = 0
        # while end < minl:
        #     for i in range(1,len(strs)):
        #         if strs[i][end]!= strs[0][end]:
        #             return strs[0][:end]
        #     end += 1
        # return strs[0][:end]

        # # 3. 分治法，时间O(s)
        # if len(strs) == 0:
        #    return ""

        # return self.lcp(strs, 0, len(strs)-1)

        # 4. 二分查找
        if not strs:
            return ""

        minL = min([len(x) for x in strs])
        l, r = 0, minL - 1
        while l <= r:
            mid = (l + r) // 2
            if self.hascommon(strs, mid):
                l = mid + 1
            else:
                r = mid - 1
        print(l, r)
        return strs[0][:l]

        # 5. 字典tree

    def lcp(self, strs, l, r):
        # 返回l和r的公共前缀字符
        if l == r:
            return strs[l]

        mid = (l + r) // 2
        lcpl = self.lcp(strs, l, mid)
        lcpr = self.lcp(strs, mid + 1, r)
        return self.common(lcpl, lcpr)

    def common(self, l, r):
        cnt = min(len(l), len(r))
        for i in range(cnt):
            if l[i] != r[i]:
                return l[:i]
        return l[:cnt]

    def hascommon(self, strs, mid):
        mode = strs[0][:mid + 1]
        for s in strs:
            if s[:mid + 1] != mode:
                return False
        return True