class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # 1. 库函数
        # nums.sort()

        # # 2. 先计算每个元素的个数，再遍历写入
        # cnt = [0, 0, 0]
        # for num in nums:
        #     cnt[num] += 1
        # index = 0
        # for i in range(len(cnt)):
        #     for j in range(cnt[i]):
        #         nums[index] = i
        #         index += 1

        # 3. 一次遍历完成调整，此处的区间均表示左闭右闭
        # nums[: le]表示0序列，le是最后一个0的索引
        # nums[le+1: i]表示1序列，i是最后一个1的索引
        # nums[gt: ]表示2序列，gt是第一个2的索引
        le, gt, i = -1, len(nums), 0
        while i < gt:  # 当i==gt时表示序列已经调整好
            if nums[i] == 0:  # le++，此时le表示的一定是1，所以交换元素后需要对i+1
                le += 1
                nums[le], nums[i] = nums[i], nums[le]
                i += 1
            elif nums[i] == 2:  # gt--，交换元素
                gt -= 1
                nums[gt], nums[i] = nums[i], nums[gt]
            else:  # 直接++
                i += 1