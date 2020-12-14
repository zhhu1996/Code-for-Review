class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """寻找顺次整数
        1. 暴力迭代
        遍历[low,high]的所有整数，判断是否满足顺次条件

        2. 生成所有满足条件的整数
        low假设有n位数字，123..n，只需要确定首位数字，就可以确定这一个整数，首位整数的范围是[low[0], 10-n]
        遍历low到high的首位数字

        3. 枚举法
        从最高位开始，选定一个1-9之间的数字，生成所有满足条件的数
        总共有9+8+7+..+1种情况
        """
        # # 方法2
        # result = []
        # n1, n2 = len(str(low)), len(str(high))
        # for i in range(n1, n2+1):
        #     if i == n1:
        #         start = int(str(low)[0])
        #     else:
        #         start = 1
        #     for j in range(start, 10-i+1):
        #         now = [str(k) for k in range(j, j+i)]
        #         now = int("".join(now))
        #         if now >= low and now <= high:
        #             result.append(now)
        # return result

        # 方法3
        result = []
        for i in range(1, 10):
            number = 0
            for j in range(i, 10):
                number = number * 10 + j
                if number >= low and number <= high:
                    result.append(number)
        result.sort()
        return result


