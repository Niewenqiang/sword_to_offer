# -*- coding:utf-8 -*-

# 矩阵中的路径

# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
# 路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
# 如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。

# 1、思路
#
# 这是一个可以用回溯法解决的典型问题。
#
# 首先，遍历这个矩阵，我们很容易就能找到与字符串str中第一个字符相同的矩阵元素ch。然后遍历ch的上下左右四个字符，
# 如果有和字符串str中下一个字符相同的，就把那个字符当作下一个字符（下一次遍历的起点），如果没有，就需要回退到上一个字符，
# 然后重新遍历。为了避免路径重叠，需要一个辅助矩阵来记录路径情况。
#
# 下面代码中，当矩阵坐标为（row，col）的格子和路径字符串中下标为pathLength的字符一样时，从4个相邻的格子（row，col-1）、
# （row-1，col）、（row，col+1）以及（row+1，col）中去定位路径字符串中下标为pathLength+1的字符。
#
# 如果4个相邻的格子都没有匹配字符串中下标为pathLength+1的字符，表明当前路径字符串中下标为pathLength的字符在矩阵中的定位不正确，
# 我们需要回到前一个字符串（pathLength-1），然后重新定位。
#
# 一直重复这个过程，直到路径字符串上所有字符都在矩阵中找到格式的位置（此时str[pathLength] == '\0'）。


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols + j] == path[0]:
                    if self.find_path(matrix, rows, cols, path[1:], i, j):
                        return True

    def find_path(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        matrix[i*cols + j] = 0
        if j+1 < cols and matrix[i*cols+j+1] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i, j+1)
        elif j-1 >= 0 and matrix[i*cols+j-1] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i, j-1)
        elif i+1 < rows and matrix[(i+1)*cols+j] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i+1, j)
        elif i-1 >= 0 and matrix[(i-1)*cols+j] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i-1, j)
        else:
            return False


s = Solution()
# print s.hasPath([['a', 'b', 'c', 'e'], ['s', 'f', 'c', 's'], ['a', 'd', 'e', 'e']], 3, 4, 'cced')
print s.hasPath(['a', 'b', 'c', 'e', 's', 'f', 'c', 's', 'a', 'd', 'e', 'e'], 3, 4, 'cced')