class ThroneInheritance:
    """王位继承顺序
    1. N叉树 + 先序遍历
    """

    def __init__(self, kingName: str):
        self.par_child = defaultdict(list)
        self.king = kingName
        self.deaths = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.par_child[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:
        # # 1. 双端队列
        # q = deque()
        # q.append(self.king)
        # orders = []
        # while len(q) > 0:
        #     cur = q.popleft()
        #     orders.append(cur)
        #     for child in self.par_child[cur][::-1]:
        #         q.appendleft(child)

        # 2. 先序遍历
        orders = []
        def pre_order(cur):
            if not cur: return
            orders.append(cur)
            for child in self.par_child[cur]:
                pre_order(child)
        
        pre_order(self.king)
        return [order for order in orders if order not in self.deaths]
        

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()