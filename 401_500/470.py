# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        i. 
        已知 rand_N() 可以等概率的生成[1, N]范围的随机数
        那么:
        (rand_X() - 1) × Y + rand_Y() ==> 可以等概率的生成[1, X * Y]范围的随机数
        即实现了 rand_XY()
        ii. 
        已知 x % y == 0, rand_x可以等概率生成[1, x]范围的随机数
        那么:
        rand_x() % y + 1 ==> 可以等概率生成[1, y]范围的随机数 
        """
        while True:
            num = (rand7()-1) * 7 + rand7() # [1,49]
            if num <= 40:
                return num % 10 + 1