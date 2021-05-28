# -*- coding:utf-8 -*-

# 问题描述：n个人（编号0~(n-1))，从0开始报数，报到(m-1)的退出，剩下的人继续从0开始报数。求胜利者的编号。


class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1:
            return -1
        res, i = 0, 2
        while i <= n:
            res = (res + m) % i
            i += 1
        return res


s = Solution()
print s.LastRemaining_Solution(13, 4)


#https://blog.csdn.net/dongyanwen6036/article/details/84892590
    
#由此，得出公式f(n)=(f(n-1)+m)%n,f(1)=0.
