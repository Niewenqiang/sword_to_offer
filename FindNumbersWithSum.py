# -*- coding:utf-8 -*-

# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，
# 输出两个数的乘积最小的。
#
# 输出描述：
#
# 对应每个测试案例，输出两个数，小的先输出。
# 1、思路
#
# 对于一个数组，我们可以定义两个指针，一个从左往右遍历（pleft），另一个从右往左遍历（pright）。
# 首先，我们比较第一个数字和最后一个数字的和curSum与给定数字sum，如果curSum < sum，那么我们就要加大输入值，
# 所以，pleft向右移动一位，重复之前的计算；如果curSum > sum，那么我们就要减小输入值，所以，pright向左移动一位，重复之前的计算；
# 如果相等，那么这两个数字就是我们要找的数字，直接输出即可。
#
# 这么做的好处是，也保证了乘积最小。


class Solution:
    def FindNumbersWithSum(self, array, sum):
        if not array:
            return []
        n = len(array)
        right = -1
        left = 0
        while left-right < n:
            curSum = array[left] + array[right]
            if curSum < sum:
                left += 1
            elif curSum == sum:
                return [array[left], array[right]]
            else:
                right -= 1
        return []


s = Solution()
print s.FindNumbersWithSum([1, 2, 3, 4, 5, 6, 7], 5)
