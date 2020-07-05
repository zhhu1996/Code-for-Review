class Solution:
    def permutation(self, s: str) -> List[str]:
        """求字符串的全排列
        1. 可以求索引的全排列，然后映射成字符串
        2. 将字符串分为2部分，逐个交换
        """

        def permutationCore(slist, index):
            if index >= len(slist):
                self.result.append("".join(slist))
                return
            for i in range(index, len(slist)):
                slist[index], slist[i] = slist[i], slist[index]
                permutationCore(slist, index + 1)
                slist[index], slist[i] = slist[i], slist[index]

        def permutationCoreV2(slist, result, visited):
            if len(result) == len(slist):
                self.result.append("".join(result))
                return
            for i in range(len(slist)):
                if visited[i]:
                    continue
                if i > 0 and slist[i] == slist[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                result.append(slist[i])
                permutationCoreV2(slist, result, visited)
                result.pop()
                visited[i] = False

        self.result = []
        visited = [False for i in range(len(s))]
        permutationCoreV2(sorted(list(s)), [], visited)
        return self.result
        # permutationCore(list(s), 0)
        # return list(set(self.result))


