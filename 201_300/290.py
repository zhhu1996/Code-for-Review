class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """单词规律
        1. 模拟
        单向满足: 借助哈希表生成pattern对应的ans, 再比较ans与s是否一致
        题意需要双向满足
        """
        def is_same(k, v, sep):
            if sep == '':
                kl = k
                vl = v.split(' ')
            else:
                kl = k.split(' ')
                vl = v
            if len(kl) != len(vl):
                return False
            exists = {}
            n = len(kl)
            for i in range(n):
                if kl[i] not in exists:
                    exists[kl[i]] = vl[i]
                else:
                    if exists[kl[i]] != vl[i]:
                        return False
            return True

        return is_same(pattern, s, '') and is_same(s, pattern, ' ')