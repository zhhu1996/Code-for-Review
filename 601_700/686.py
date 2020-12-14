class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        """KMP"""
        k = (len(B)-1)//len(A) + 1
        if B in k*A :
            return k
        if B in (k+1)*A:
            return k+1
        return -1