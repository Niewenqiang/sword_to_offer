# -*- coding:utf-8 -*-

# 数据流中的中位数

# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
# 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。


class Solution:
    def __init__(self):
        self.res = []

    def Insert(self, num):
        # write code here
        self.res.append(num)

    def GetMedian(self):
        # write code here
        self.res.sort()
        length = len(self.res)
        if length % 2 == 0:
            return (self.res[length / 2 - 1] + self.res[length / 2]) / 2.0
        else:
            return self.res[length / 2]


s = Solution()
s.Insert(0)
s.Insert(1)
s.Insert(2)
s.Insert(3)
s.Insert(4)
print s.GetMedian()
s.Insert(5)
print s.GetMedian()


