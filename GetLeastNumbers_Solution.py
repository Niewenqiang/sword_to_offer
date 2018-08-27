# -*- coding:utf-8 -*-

# 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
# 1、思路
#
# 最简单的方法就是先排序，然后在遍历输出最小的K个数，方法简单粗暴。

# a = [4,5,1,6,2,7,3,8]
#
# print sorted(a)[:4]


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k:
            return []
        tmp = sorted(tinput[:k])
        for each in tinput[k:]:
            index = k - 1
            flag = False
            while index >= 0 and tmp[index] > each:
                index -= 1
                flag = True
            if flag == True:
                tmp.insert(index+1, each)
                tmp.pop()
        return tmp


s = Solution()
print s.GetLeastNumbers_Solution([1, 11, 5, 6, 7, 8, 9], 4)
