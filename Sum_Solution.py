# -*- coding:utf-8 -*-


# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
# 1、思路
# 没什么好说的，这是一道超级无敌送分题，使用递归即可。


class Solution:
    def summ(self, n):
        return n and (n+self.summ(n-1))

s = Solution()
print s.summ(2)


class Solution2:
    def Sum_Solution(self, n):
        return sum(list(range(1, 1 + n)))


class Solution3:
    def Sum_Solution(self, n):
        def f(x, y):
            return x+y
        return reduce(f, range(1, n+1))
