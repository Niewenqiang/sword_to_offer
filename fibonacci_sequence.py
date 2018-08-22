# -*- coding:utf-8 -*-

# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。（n<=39）

# 1、思路
# 这道题递归很好写，但是存在很严重的效率问题。我们以求解f(10)为例类分析递归的求解过程。
# 想求f(10)，需要先求得f(9)和f(8)。同样，想求得f(9)，需要先求的f(8)和f(7)....我们可以用树形结构来表示这种依赖关系
# 我们不难发现在这棵树中有很多结点是重复的，而且重复的结点数会随着n的增加而急剧增加，这意味计算量会随着n的增加而急剧增大。
# 事实上，递归方法计算的时间复杂度是以n的指数的方式递增的。
# 所以，使用简单的循环方法来实现。

class Solution:
    def Fibonacci(self, n):
        if n <= 1:
            return n
        first, second, third = 0, 1, 0
        for i in range(2, n+1):
            third = first + second
            first = second
            second = third
        return third

s = Solution()
print s.Fibonacci(8)

# import time
# while True:
#     x = int(raw_input())
#     if x < 0:
#         print '请输入大于0的数'
#         time.sleep(1)
#     elif x>39:
#         print '不大于39'
#         time.sleep(1)
#     else:
#         sum = [0,1]
#         if x == 0:
#             print 0
#         elif x == 1:
#             print 1
#         else:
#             for i in range(2, x+1):
#                 z = sum[i-1]+sum[i-2]
#                 sum.append(z)
#             print sum[-1]




