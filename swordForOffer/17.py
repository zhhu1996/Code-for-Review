class Solution:
    def printNumbers(self, n: int) -> List[int]:
        """全排列打印"""

        self.array = []

        def generateArray(array, index, n):
            if index == n:
                for j in range(len(array)):
                    if array[j] != '0':
                        self.array.append((int)(''.join(array[j:])))
                        break
                return
            for i in range(10):
                array[index] = str(i)
                generateArray(array, index+1, n)
                array[index] = '0'

        array = ['0' for i in range(n)]
        generateArray(array, 0, n)
        return self.array