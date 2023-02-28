class Solution:
    def compress(self, chars: List[str]) -> int:
        """压缩字符串
        1. 双指针
        nums[0:j]表示压缩完的字符
        """
        if len(chars) == 1: return 1
        last = ''
        j = -1
        cnt = 0
        for i in range(len(chars)):
            if not last:
                last = chars[i]
                cnt += 1
            else:
                if chars[i] == last:
                    cnt += 1
                else:
                    j += 1
                    chars[j] = last
                    last = chars[i]
                    tmp = str(cnt)
                    if tmp == '1':
                        continue
                    for k in tmp:
                        j += 1
                        chars[j] = k
                    cnt = 1
        j += 1
        chars[j] = last
        tmp = str(cnt)
        if tmp != '1':
            for k in tmp:
                j += 1
                chars[j] = k
        return j+1