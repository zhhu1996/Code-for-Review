class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        """密钥格式化
        1. 将所有非-字符挑选出来，k个一组, 第一个分组的元素个数为len - len//K*K
        """
        words = []
        for c in S:
            if c != "-":
                words.append(c.upper())
        length = len(words)
        result = []
        if length//K * K == length:
            splits = length // K
        else:
            splits = length // K + 1
        firstLength = 0
        if splits > length // K:
            firstLength = length - (splits-1)*K
        for i in range(firstLength):
            result.append(words[i])
        if firstLength > 0 and firstLength != length:
            result.append("-")
        j = firstLength
        t = K
        while j < length:
            result.append(words[j])
            t -= 1
            if t == 0 and j != length-1:
                result.append("-")
                t = K
            j += 1
        return "".join(result)



