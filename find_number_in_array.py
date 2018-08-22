# -*- coding:utf-8 -*-

# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# 1、思路
# 首先选取数组中右上角的数字。如果该数字等于要查找的数字，查找过程结束；如果该数字大于要查找的数组，剔除这个数字所在的列；
# 如果该数字小于要查找的数字，剔除这个数字所在的行。也就是说如果要查找的数字不在数组的右上角，
# 则每一次都在数组的查找范围中剔除一行或者一列，这样每一步都可以缩小查找的范围，直到找到要查找的数字，或者查找范围为空。
# 2、举例
# 如果在一个二维数组中找到数字7，则返回true，如果没有找到，则返回false

array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]

# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         # write code here
#         rows = len(array)
#         cols = len(array[0])
#         if rows > 0 and cols > 0:
#             row = 0
#             col = cols - 1
#             while row < rows and col >= 0:
#                 if target == array[row][col]:
#                     return True
#                 elif target < array[row][col]:
#                     col -= 1
#                 else:
#                     row += 1
#         return False


class Solution:
    def Find(self, target, array):
        if array == []:
            return False
        else:
            x = len(array[0])
            y = len(array)
            z = 0
            while x >= 1 and z <= y-1:
                if array[z][x-1] == target:
                    return True
                elif array[z][x-1] > target:
                    x -= 1
                else:
                    z += 1
            return False


s = Solution()
print s.Find(6, array)


