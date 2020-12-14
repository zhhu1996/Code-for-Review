from collections import Counter, defaultdict


class Solution:
    def balancedString(self, s: str) -> int:
        """替换子串得到平衡字符串
        注意被替换的子串需要是连续的;
        总共四个字符，只需要考虑出现次数>n//4个字符即可
        当窗口内不包含需要替换的字符总数时，r++
        否则l++
        统计最短长度
        """
        n = len(s)
        counter = Counter(s)
        result = n
        table = defaultdict(int)
        for k, v in counter.items():
            counter[k] = max(0, v-n//4)
        i, j = 0, 0
        while j < n:
            table[s[j]] += 1
            while i < n and table["Q"] >= counter["Q"] and table["W"] >= counter["W"] and table["E"] >= counter["E"] and table[
                "R"] >= counter["R"]:
                table[s[i]] -= 1
                result = min(result, j - i + 1)
                i += 1
            j += 1
        return result
