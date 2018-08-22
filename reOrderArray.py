# -*- coding:utf-8 -*-

# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# 所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
# 1、思路
#
# 创建双向队列，遍历数组，奇数前插入，偶数后插入。最后使用assign方法实现不同容器但相容的类型赋值。


from collections import deque
class Solution:
    def reOrderArray(self, array):
        odd = deque()
        l = len(array)
        for i in range(l):
            if array[l-i-1] % 2 != 0:
                odd.appendleft(array[-i-1])
            if array[i] % 2 == 0:
                odd.append(array[i])
        return list(odd)



s = Solution()
print s.reOrderArray([1,2,3,4,5,6,7,8,9])

# a = [1,2,3,4,5,6,7,8,9]
# b = []
# c = []
# d = []
# for i in a:
#     if i%2 == 1:
#         b.insert(0,i)
#     else:
#         c.insert(0,i)
# for i in range(len(a)):
#     if b:
#         d.append(b.pop())
#     else:
#         d.append(c.pop())
#
# print d
