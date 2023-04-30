class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """比较含退格的字符串
        1. 栈, 时间复杂度O(n), 空间复杂度O(n)

        2. 双指针模拟栈, 时间复杂度O(n), 空间复杂度O(n)
        
        3. 双指针 + 计数器, 时间复杂度O(n), 空间复杂度O(1)
            i. 当前字符是'#'
           ii. 当前字符不是'#', 且计数器不为0 -> 跳过
          iii. 当前字符不是'#', 且计数器为0 -> 比较
        """
        # 3.
        i, j = len(s)-1, len(t)-1
        cs, ct = 0, 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    i -= 1
                    cs += 1
                elif cs > 0:
                    i -= 1
                    cs -= 1
                else:
                    break
            while j >= 0:
                if t[j] == '#':
                    j -= 1
                    ct += 1
                elif ct > 0:
                    j -= 1
                    ct -= 1
                else:
                    break
            if (i >= 0 and j >= 0 and s[i] != t[j]) or (i >= 0 and j < 0) or (i < 0 and j >= 0):
                return False
            i -= 1
            j -= 1
        return True