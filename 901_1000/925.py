class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """长按键入
        1. 双指针
        p1 = "saeed", p2 = "ssaaedd", i = 1, j = 1
        if p1[i] == p2[j]: i++, j++
        else:
            if p2[j] != p2[j-1]: return false
            else: j++
        """
        if not name or not typed:
            return False
        if name[0] != typed[0]:
            return False
        i, j = 1, 1
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if typed[j-1] != typed[j]:
                    return False
                else:
                    j += 1
        if i < len(name):
            return False
        while j < len(typed):
            if typed[j] != typed[j-1]:
                return False
            j += 1
        return True