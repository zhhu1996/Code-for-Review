class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1. 二分, 时间复杂度O(nlogn)
        先对第一行进行二分, 查找>=target的首个元素, 再对之前的每一列进行二分查找
        """
        m, n = len(matrix), len(matrix[0])
        # 0行
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if matrix[0][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if l < n and matrix[0][l] == target:
            return True
        # 0..k列
        for col in range(0, l):
            lo, hi = 0, m-1
            while lo <= hi:
                mid = (lo + hi) // 2
                if matrix[mid][col] == target:
                    return True
                elif matrix[mid][col] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False