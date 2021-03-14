class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """下一个更大元素 II
        方法一: 暴力解法
        时间复杂度: O(n^2)

        方法二: 经过优化的暴力解法
        假设对于当前元素x_i，对应的下一个更大元素是x_k，那么可知x_k > x_i > x_(i+1) > x_(i+2) > ... > x_(k-1)
        那么对于x_(i+1)，需要寻找下一个更大元素，需要查询的序列为[x_(i+2),x_(i+3),...,x_k]
        时间复杂度比方法一低，但是仍然是O(n^2)

        方法三: 单调堆栈
        每次我们移动到数组中的一个新的位置i，我们就将当前单调栈中所有对应值小于nums[i]的下标弹出单调栈，这些值的下一个更大元素即为nums[i]
        """
        # # 方法一
        # if not nums:
        #     return []
        # N = len(nums)
        # result = []
        # for i in range(N):
        #     j = i + 1
        #     while j < i + N:
        #         if nums[j % N] > nums[i]:
        #             result.append(nums[j % N])
        #             break
        #         j += 1
        #     if j == i + N:
        #         result.append(-1)
        # return result

        # # 方法二
        # if not nums:
        #     return []
        # N = len(nums)
        # result = []
        # last = -1
        # for i in range(N):
        #     j = i+1
        #     end = i+N
        #     if last != -1:
        #         end = min(end,last+N+1)
        #     while j < end:
        #         if nums[j%N] > nums[i]:
        #             result.append(nums[j%N])
        #             last = j%N
        #             break
        #         j += 1
        #     if j == end:
        #         result.append(-1)
        # return result

        # 方法三
        table = {}
        stack = []
        for k in range(2):
            for i in range(len(nums)):
                if k == 0:
                    if not stack:
                        stack.append([i,nums[i]])
                        continue
                    while stack and stack[-1][-1] < nums[i]:
                        tmp = stack.pop(-1)
                        table[tmp[0]] = nums[i]
                    stack.append([i,nums[i]])
                else:
                    while stack and stack[-1][-1] < nums[i]:
                        if i == stack[-1][0]:
                            break
                        tmp = stack.pop(-1)
                        table[tmp[0]] = nums[i]
        while stack:
            table[stack.pop(-1)[0]] = -1
        result = []
        for j in range(len(nums)):
            result.append(table[j])
        return result