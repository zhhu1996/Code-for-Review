class Solution:
    def calculate(self, s: str) -> int:
        """基本计算器III
        1. 双栈 + 字符串
        """
        ops, nums = [], []

        def calc_op(num1, num2, op):
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
            elif op == '/':
                ans = num1 // num2
                return ans if ans >= 0 else ans+1            

        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = int(s[i])
                while i+1 < len(s) and s[i+1].isdigit():
                    num = num*10 + int(s[i+1])
                    i += 1
                nums.append(num)
            elif s[i] in ['+', '-']:
                while ops and ops[-1] in ['+', '-', '*', '/']:
                    op = ops.pop()
                    num2 = nums.pop()
                    num1 = nums.pop()
                    nums.append(calc_op(num1, num2, op))
                ops.append(s[i])
            elif s[i] in ['*', '/']:
                while ops and ops[-1] in ['*', '/']:
                    op = ops.pop()
                    num2 = nums.pop()
                    num1 = nums.pop()
                    nums.append(calc_op(num1, num2, op))
                ops.append(s[i])
            elif s[i] == '(':
                ops.append(s[i])
            elif s[i] == ')':
                while ops and ops[-1] != '(':
                    op = ops.pop()
                    num2 = nums.pop()
                    num1 = nums.pop()
                    nums.append(calc_op(num1, num2, op))
                ops.pop()
            else: 
                print('wrong input')
            i += 1
        while ops:
            op = ops.pop()
            num2 = nums.pop()
            num1 = nums.pop()
            nums.append(calc_op(num1, num2, op))
        assert len(nums) + len(ops) == 1
        return nums[0]