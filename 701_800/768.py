class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """最多能完成排序的块 II
        1. dp + 贪心, 时间复杂度O(n)
        lmax[i] = arr[0..i]最大值; rmin[i] = arr[i..n-1]最小值
        对于任意点i, 只要lmax[i] <= rmin[i+1], 即可在i与i+1之间截断

        2. 排序 + 哈希表, 时间复杂度O(nlogn)
        比较两个子数组arr, sorted(arr), 如果在某一个窗口内频次之差为0, 那么可分出一个新的块出来

        3. 单调栈, 时间复杂度O(n)
        遍历arr, 如果比栈顶元素大则入栈, 可作为独立块; 如果比栈顶元素小, 则需要合并, 也就是找到除栈顶外第一个小于等于它的元素
        """
        # # 1.
        # n = len(arr)
        # lmax = [0]*n
        # rmin = [0]*n
        # for i in range(n):
        #     if i == 0: lmax[i] = arr[i]
        #     else: lmax[i] = max(lmax[i-1], arr[i])
        # for j in range(n-1, -1, -1):
        #     if j == n-1: rmin[j] = arr[j]
        #     else: rmin[j] = min(rmin[j+1], arr[j])
        # ans = 0
        # for i in range(n-1):
        #     if lmax[i] <= rmin[i+1]:
        #         ans += 1
        # return ans + 1


        # # 2.
        # cnt = Counter()
        # ans = 0
        # for x, y in zip(arr, sorted(arr)):
        #     cnt[x] += 1
        #     if cnt[x] == 0:
        #         del cnt[x]
        #     cnt[y] -= 1
        #     if cnt[y] == 0:
        #         del cnt[y]
        #     if len(cnt) == 0:
        #         ans += 1
        # return ans


        # 3.
        stack = []
        for x in arr:
            if not stack or x >= stack[-1]:
                stack.append(x)
            else:
                mx = stack.pop()
                while stack and x < stack[-1]:
                    stack.pop()
                stack.append(mx)
        return len(stack)