class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        用哈希表记录order中每个字母的位置，然后对words中的单词逐个比较
        """
        table = {}
        for index, value in enumerate(order):
            table[value] = index
        table[""] = 0
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j == len(words[i+1]) or table[words[i][j]] > table[words[i+1][j]]:
                    return False
                elif table[words[i][j]] < table[words[i+1][j]]:
                    break
                else:
                    continue
        return True 