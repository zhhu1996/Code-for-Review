# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    """扁平化嵌套列表迭代器
    方法1: 利用链表或者列表生成迭代的序列

    方法2: 利用堆栈模拟方法1
    """

    def __init__(self, nestedList: [NestedInteger]):
        # # 方法1
        # self.array = nestedList
        # self.result = []
        # self.iterate(self.array)
        # self.length = len(self.result)
        # self.index = 0

        # 方法2
        self.stack = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def iterate(self, arr):
        if not arr:
            return
        for i in range(len(arr)):
            if arr[i].isInteger():
                self.result.append(arr[i].getInteger())
            else:
                self.iterate(arr[i].getList())

    def next(self) -> int:
        # # 方法1
        # cur = self.index
        # self.index += 1
        # return self.result[cur]

        # 方法2
        return self.stack.pop()

    def hasNext(self) -> bool:
        # # 方法1
        # return self.index < self.length

        # 方法2
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True
            cur_list = cur.getList()
            self.stack.pop()
            for i in range(len(cur_list) - 1, -1, -1):
                self.stack.append(cur_list[i])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
