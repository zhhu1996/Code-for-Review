class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """搜索推荐系统
        1. 暴力匹配，对于候选集里面的所有字符串，进行暴力匹配
        2.
        """
        if not products or not searchWord:
            return []
        products.sort()
        result = []
        for i in range(len(searchWord)):
            temp = []
            k = 0
            for j in range(len(products)):
                if searchWord[:i+1] == products[j][:i+1]:
                    k += 1
                    temp.append(products[j])
                    if k == 3:
                        break
            result.append(temp)
        return result
