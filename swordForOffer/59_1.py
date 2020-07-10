from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """滑动窗口的最大值
        1. 暴力法，时间复杂度O(nk)

        2. 用队列来存储当前滑动窗口的最大值，时间复杂度O(n)
        将数组分为两端，第一段不需要判断队列中的元素是否过期，第二段需要判断
        第一段：
            在更新最大元素的时候，从队尾开始比较，将小于当前元素的全部出队；
        第二段：
            先判断最大元素是否是过期的（不在滑动窗口内），因此队列中存放元素的索引；
            在更新最大元素的时候，从队尾开始比较，将小于当前元素的全部出队；
        """
        if not nums or k <= 0:
            return []

        result = []
        q = deque()
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)  # 队列中存放索引
        result.append(nums[q[0]])
        for i in range(k, len(nums)):
            if q and q[0] + k <= i: # 只需要判断一次过期的元素
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            result.append(nums[q[0]])
        return result
