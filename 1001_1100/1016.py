class Solution:
    def queryString(self, s: str, n: int) -> bool:
        """子串能表示从 1 到 N 数字的二进制串
        1. 枚举子串
        枚举所有子串, 如果在[1,n]内且没出现过, 则加入集合, 时间复杂度O(m*logn*logn), m为字符串s的长度
        # int(str, base) => 以base作为str的进制, 解析为十进制数, 时间复杂度O(m)
        => 求十进制可以在O(1)时间内实现

        2. 枚举n, 时间复杂度O(min(m,n)*m*logmin(m,n))
        """
        # 1.
        nums = set()
        s = list(map(int, s)) 
        for i in range(len(s)):
            for j in range(i, len(s)):
                # target = int(s[i:j+1], 2) 
                target = s[j] if j == i else (target << 1) | s[j]
                if target > n: break
                elif target > 0 and target not in nums:
                    nums.add(target)
        return len(nums) == n


        # # 2.
        # for i in range(1, n+1):
        #     if bin(i)[2:] not in s: # 如果len(target) > len(s), 直接返回False
        #         return False
        # return True