class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # # 1. 二分查找模版1
        # left, right = 0, len(letters)-1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if letters[mid] < target:
        #         left = mid + 1
        #     elif letters[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = right = mid
        #         break
        # if left <= right: # 找到了
        #     while left < len(letters)-1 and letters[left+1]==target:
        #         left += 1
        #     return letters[(left+1) % len(letters)]
        # else: # left = right + 1，未找到
        #     return letters[left % len(letters)]

        # 2. 二分查找模版2
        left, right = 0, len(letters)
        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left % len(letters)]