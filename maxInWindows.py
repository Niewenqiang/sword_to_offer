# -*- coding:utf-8 -*-

# 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
# 那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}。

# 我们可以使用一个双端队列deque。
# 我们可以用STL中的deque来实现，接下来我们以数组{2,3,4,2,6,2,5,1}为例，来细说整体思路。
#
# 数组的第一个数字是2，把它存入队列中。第二个数字是3，比2大，所以2不可能是滑动窗口中的最大值，因此把2从队列里删除，
# 再把3存入队列中。第三个数字是4，比3大，同样的删3存4。此时滑动窗口中已经有3个数字，而它的最大值4位于队列的头部。
#
# 第四个数字2比4小，但是当4滑出之后它还是有可能成为最大值的，所以我们把2存入队列的尾部。下一个数字是6，比4和2都大，
# 删4和2，存6。就这样依次进行，最大值永远位于队列的头部。
#
# 但是我们怎样判断滑动窗口是否包括一个数字？应该在队列里存入数字在数组里的下标，而不是数值。
# 当一个数字的下标与当前处理的数字的下标之差大于或者相等于滑动窗口大小时，这个数字已经从窗口中滑出，可以从队列中删除。


# class Solution:
#     def maxInWindows(self, matrix, n):
#         result = []
#         for i in range(len(matrix)-n+1):
#             result.append(max(matrix[i:i+n]))
#         return result


class Solution:
    def maxInWindows(self, num, size):
        if not num:
            return []
        if size > len(num) or size < 1:
            return []
        if size == 1:
            return num
        temp = [0]
        res = []
        for i in range(len(num)):
            if i - temp[0] >= size:
                temp.pop(0)
            while len(temp) > 0 and num[i] >= num[temp[-1]]:
                temp.pop()
            if len(temp) < size-1:
                temp.append(i)
            if i >= size-1:
                res.append(num[temp[0]])
        return res


s = Solution()
print s.maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3)



