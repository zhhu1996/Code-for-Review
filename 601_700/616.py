class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        """ 给字符串添加加粗标签
        1. 将问题转换成求区间的并集
        分为3个步骤：
            对于每个字符串p，生成与s的交集区间，时间复杂度O(Ls*Lp);
            合并区间，时间复杂度O(n);
                1. 根据起点的大小排序
                2. 合并条件：当前节点的终点 >= 下一个节点的起点 or 当前节点的终点 +1 == 下一个节点的起点
                3. 合并操作：起点不变，终点取两个终点的较大值
            通过双指针根据原字符串s与交集区间输出字符串;
            1. 指针i指向原字符串中的索引，指针j指向交集列表的索引
            2. 递增指针i，分为四种情况处理输出字符
                i. j >= len(result)，说明交集区间已经遍历完成，直接打印s的字符即可
                ii. j < len(result)，需要考虑i是否与交集的起点、终点重合
                    a. i与起点、终点都相等
                    b. i与起点相等
                    c. i与终点相等
                    d. i与起点、终点都不相等
        """
        unionList = []

        def getUnion(s, p, result):
            # 对于每个字符串p，生成与s的交集区间，时间复杂度O(Ls*Lp)
            for i in range(len(s) - len(p) + 1):
                flag = True
                for j in range(len(p)):
                    if s[i + j] != p[j]:
                        flag = False
                        break
                if flag:
                    result.append([i, i + len(p) - 1])

        def getResult(s, p, unionList):
            """ 合并区间，时间复杂度O(n)
            1. 根据起点的大小排序
            2. 合并条件：当前节点的终点 >= 下一个节点的起点 or 当前节点的终点 +1 == 下一个节点的起点
            3. 合并操作：起点不变，终点取两个终点的较大值
            """
            result = []
            n = len(unionList)
            i = 1
            unionList.sort(key=lambda x: x[0])
            start, end = unionList[0][0], unionList[0][1]
            while i < n:
                if end >= unionList[i][0] or end == unionList[i][0] - 1:
                    end = max(end, unionList[i][1])
                else:
                    result.append([start, end])
                    start, end = unionList[i][0], unionList[i][1]
                i += 1
            result.append([start, end])
            return result

        def printString(s, result):
            """ 根据原字符串s与交集区间输出字符串
            双指针法：
            1. 指针i指向原字符串中的索引，指针j指向交集列表的索引
            2. 递增指针i，分为四种情况处理输出字符
                i. j >= len(result)，说明交集区间已经遍历完成，直接打印s的字符即可
                ii. j < len(result)，需要考虑i是否与交集的起点、终点重合
                    a. i与起点、终点都相等
                    b. i与起点相等
                    c. i与终点相等
                    d. i与起点、终点都不相等
            """
            ns = []
            j = 0
            print(result)
            for i in range(len(s)):
                if j < len(result):
                    if i == result[j][0] and i == result[j][1]:
                        ns.append("<b>")
                        ns.append(s[i])
                        ns.append("</b>")
                        j += 1
                    elif i == result[j][0]:
                        ns.append("<b>")
                        ns.append(s[i])
                    elif i == result[j][1]:
                        ns.append(s[i])
                        ns.append("</b>")
                        j += 1
                    else:
                        ns.append(s[i])
                else:
                    ns.extend(list(s[i:]))
                    break
            return "".join(ns)

        for p in dict:
            getUnion(s, p, unionList)
        if not unionList:
            return s
        result = getResult(s, p, unionList)
        return printString(s, result)






