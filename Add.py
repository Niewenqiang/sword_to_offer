# -*- coding:utf-8 -*-

# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。


# class Solution:
#     def Add(self, num1, num2):
#         return sum([num1, num2])


class Solution:
    def Add(self, num1, num2):

        while num2 != 0:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = temp & 0xFFFFFFFF
        return num1 if num1 >> 31 == 0 else num1 - 4294967296

    
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        while num2:
            res = (num1 ^ num2) & 0xffffffff
            move = ((num1 & num2) << 1) & 0xffffffff
            num1 = res
            num2 = move
        if num1 <= 0x7fffffff:
            res = num1
        else:
            res = ~(num1 ^ 0xffffffff)
        return res
    
    
s = Solution()
print s.Add(1, -2)
