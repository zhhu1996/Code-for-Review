class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        table = {}
        for x in candies:
            if x in table:
                table[x] += 1
            else:
                table[x] = 1
        half = len(candies)//2
        if half <= len(table):
            return half
        else:
            return len(table)