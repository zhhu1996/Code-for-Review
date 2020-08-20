def getFirstTarget(nums, length, start, end, target):
    if not nums:
        return -1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            if mid > 0 and nums[mid] == nums[mid - 1]:
                end = mid - 1
            else:
                return mid


def getLastTarget(nums, length, start, end, target):
    if not nums:
        return -1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            if mid < length - 1 and nums[mid] == nums[mid + 1]:
                start = mid + 1
            else:
                return mid


print(getFirstTarget([1,4,4,4,5,6],6,0,5,4))

print(getLastTarget([1,4,4,4,5,6],6,0,5,4))