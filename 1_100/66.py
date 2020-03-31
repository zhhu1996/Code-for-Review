class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # # 从最低位依次处理，一直到最高位
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            # 非第一位更新规则
            if digits[i] + carry >= 10:
                digits[i] = digits[i] + carry - 10
                carry = 1
            else:
                digits[i] = digits[i] + carry
                carry = 0
            # 最高位特殊处理
            if i == 0 and carry == 1:
                digits.insert(0, 1)
        return digits