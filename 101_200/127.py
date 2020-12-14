from queue import Queue
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        1. Dijkstra算法：首先初始化S、U集合，S为已找到单源最短路径的点集合，U为剩余的点的集合
        每次从S中挑选一个距离最短的点加入到S中，并更新U中的距离

        2. 广度优先遍历算法：
        如何存储图最快？如果遍历每个单词找每个单词的邻近状态，时间复杂度是O(n*n*wordLen)，n是单词的个数，wordLen是每个单词的长度，
        用字典存储每个单词的通配模式，值是图中满足条件的节点. (word[:j]+"*"+word[j+1:])，j是当前需要变换的元素
        """
        # 1. 使用暴力dijkstra算法对于有很多节点的图会超时
        # if endWord not in wordList:
        #     return 0
        # pointSet = wordList.copy()
        # pointSet.append(beginWord)
        # n = len(pointSet)
        # graph = [[float("inf")] * n for i in range(n)]
        # # 建图
        # # for i in range(n - 1):
        # #     for j in range(i + 1, n):
        # #         length = len(pointSet[i])
        # #         cnt = 0
        # #         for k in range(length):
        # #             if pointSet[i][k] == pointSet[j][k]:
        # #                 cnt += 1
        # #         if cnt == length - 1:
        # #             graph[i][j] = 1
        # #             graph[j][i] = 1
        # #         else:
        # #             graph[i][j] = float("inf")
        # #             graph[j][i] = float("inf")
        # for i in range(n):
        #     graph[i][i] = 0
        #     for j in range(len(pointSet[i])):
        #         temp = pointSet.copy()
        #         for c in range(97, 123):
        #             temp[j] = c
        #             if temp in pointSet:
        #                 index = pointSet.index(temp)
        #                 graph[i][index] = 1
        #                 graph[index][i] = 1
        # start, end = n - 1, pointSet.index(endWord)
        # visited = [False] * n
        # visited[start] = True
        # distance = [float("inf") for i in range(n)]
        # for i in range(n):
        #     distance[i] = graph[start][i]
        # for it in range(n - 1):
        #     minDisatnce = float("inf")
        #     minPoint = -1
        #     for i in range(n):
        #         if not visited[i] and distance[i] < minDisatnce:
        #             minDisatnce = distance[i]
        #             minPoint = i
        #     visited[minPoint] = True
        #     for i in range(n):
        #         if not visited[i] and distance[i] > distance[minPoint] + graph[minPoint][i]:
        #             distance[i] = distance[minPoint] + graph[minPoint][i]
        # if distance[end] == float("inf"):
        #     return 0
        # return distance[end] + 1

        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        L = len(endWord)
        N = len(wordList)
        # 建图
        graph = defaultdict(list)
        for word in wordList:
            for j in range(L):
                key = word[:j] + "*" + word[j+1:]
                graph[key].append(word)
        queue = Queue(10000)
        visited = {beginWord: True}
        level = 1
        queue.put((beginWord, level))
        while not queue.empty():
            word, level = queue.get()
            for j in range(L):
                key = word[:j] + "*" + word[j+1:]
                for w in graph[key]:
                    if w == endWord:
                        return level + 1
                    if w not in visited:
                        visited[w] = True
                        queue.put((w, level+1))
        return 0








