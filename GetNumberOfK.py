# -*- coding:utf-8 -*-

# 数字在排序数组中出现的次数


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)


s = Solution()
print s.GetNumberOfK([1, 2, 3, 4, 5, 3], 3)
