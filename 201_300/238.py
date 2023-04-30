class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """除自身以外数组的乘积
        1. 前缀积 + 后缀积

        2. 除法
        计算非0值的乘积与所有值的乘积, 后通过除法计算目标值
        """
        # 1.
        n = len(nums)
        cumprod = [1]*(n+1)
        for i in range(1, n+1):
            cumprod[i] = cumprod[i-1]*nums[i-1]
        postprod = [1]*(n+1)
        for i in range(n-1, -1, -1):
            postprod[i] = postprod[i+1]*nums[i]
        ans = []
        for i in range(n):
            ans.append(cumprod[i]*postprod[i+1])
        return ans


        # # 2.
        # prod1, prod2 = 1, 1
        # zeros = 0
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] == 0:
        #         prod1 = 0
        #         zeros += 1
        #     else:
        #         prod1 *= nums[i]
        #         prod2 *= nums[i]
        # ans = [0]*n
        # for i in range(n):
        #     if nums[i] == 0:
        #         if zeros == 1:
        #             ans[i] = prod2
        #         else:
        #             ans[i] = 0
        #     else:
        #         if zeros > 0:
        #             ans[i] = 0
        #         else:
        #             ans[i] = prod1 // nums[i]
        # return ans