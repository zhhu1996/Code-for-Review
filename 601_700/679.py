class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        """24点游戏
        1. 回溯
        """
        n = len(cards)
        if n == 1:
            return abs(cards[0]-24) < 10**(-6)
        is_valid = False
        for i in range(n-1):
            for j in range(i+1, n): 
                a = cards[i]
                b = cards[j]
                next_cards = []
                for k in range(n):
                    if k != i and k != j:
                        next_cards.append(cards[k])
                # +
                is_valid = is_valid or self.judgePoint24(next_cards+[a+b])
                # -
                is_valid = is_valid or self.judgePoint24(next_cards+[a-b])
                is_valid = is_valid or self.judgePoint24(next_cards+[b-a])
                # *
                is_valid = is_valid or self.judgePoint24(next_cards+[a*b])
                # /
                if b != 0:
                    is_valid = is_valid or self.judgePoint24(next_cards+[a/b])
                if a != 0:
                    is_valid = is_valid or self.judgePoint24(next_cards+[b/a])
                if is_valid:
                    return True
        return False