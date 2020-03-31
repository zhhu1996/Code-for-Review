class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. 将所有元素存入一个列表，对列表进行二分搜索

        # 2. 依据1的思想，但是并不会新建立一个数组，通过以下公式转换
        # row = index // cols, col = index % cols
        if not matrix or not matrix[0]: # 矩阵判空
            return False
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows*cols-1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid // cols][mid % cols] == target:
                return True
            elif matrix[mid // cols][mid % cols] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

        # 3. 在矩阵中进行两次二分搜索
        # if not matrix or not matrix[0]: # 矩阵判空
        #     return False
        # rows, cols = len(matrix), len(matrix[0])
        # searchArray = []
        # for i in range(rows):
        #     searchArray.append(matrix[i][-1])
        # left, right = 0, len(searchArray) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if searchArray[mid] == target:
        #         return True
        #     elif searchArray[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # # 防止溢出，很关键
        # row = min(left, rows - 1)
        # left, right = 0, cols - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if matrix[row][mid] == target:
        #         return True
        #     elif matrix[row][mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return False