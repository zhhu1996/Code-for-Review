class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """计算各个位数不同的数字个数
        1. 迭代法
        从1开始递增，判断是否满足条件, 超时

        2. 回溯法
        生成一个n位的数组，每个位置可以填0-9这十个数字，求n个元素的全排列即可，注意首位不能是0

        3. 动态规划
        排列组合：n位有效数字 = 每一位都从 0~9 中选择，且不能以 0 开头
         * 1位数字：0~9                       10
         * 2位数字：C10-2，且第一位不能是0      9 * 9
         * 3位数字：C10-3，且第一位不能是0      9 * 9 * 8
         * 4位数字：C10-4，且第一位不能是0      9 * 9 * 8 * 7
         * ... ...
         * 最后，总数 = 所有 小于 n 的位数个数相加

        """
        # # 方法1
        # cnt = 0
        # def judge(number):
        #     return len(set(number)) == len(number)
        #
        # for i in range(10**n):
        #     if judge(str(i)):
        #         cnt += 1
        # return cnt

        # # 方法2
        # self.result = 0
        #
        # def judge(string):
        #     return len(set(string)) == len(string)
        #
        # def dfs(n, index, path, visited):
        #     if index == n:
        #         if path and judge(str(int("".join(path)))):
        #             self.result += 1
        #         return
        #     for i in range(10):
        #         if visited[i] and i != 0:
        #             continue
        #         visited[i] = True
        #         path.append(str(i))
        #         dfs(n, index + 1, path, visited)
        #         visited[i] = False
        #         path.pop()
        #
        # visited = [False] * 10
        # dfs(n, 0, [], visited)
        # if n == 0:
        #     return 1
        # return self.result

        # 方法3
        if n == 0:
            return 1
        total = 10
        base = 9
        for i in range(2, n + 1):
            total += base * (11 - i)
            base = base * (11 - i)
        return total

