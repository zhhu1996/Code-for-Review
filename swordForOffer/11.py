class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """二分查找、考虑特殊情况"""
        l, r = 0, len(numbers)-1
        mid = l
        while numbers[l] >= numbers[r]:
            if r - l == 1:
                mid = r
                break
            mid = (l + r) // 2
            # 特殊情况：l、r、mid对应元素均相等
            if numbers[mid] == numbers[l] and numbers[mid] == numbers[r]:
                result = numbers[l]
                for k in range(l, r+1):
                    result = min(result, numbers[k])
                return result

            if numbers[mid] >= numbers[l]:
                l = mid
            elif numbers[mid] <= numbers[r]:
                r = mid

        return numbers[mid]
