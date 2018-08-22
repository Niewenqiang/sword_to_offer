# -*- coding:utf-8 -*-

# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# 1、思路
#
# 当指数为负数的时候，可以先对指数求绝对值，然后算出次方的结果之后再取倒数。
# 如果底数为0，则直接返回0。此时的次方在数学上是没有意义的。


class Solution:
    def power(self, base, exponent):
        result = 1
        if base == 0:
            return False
        for i in range(abs(exponent)):
            result *= base
        if exponent < 0:
            result = 1/result
        return result

s = Solution()
print s.power(float(2), -4)

