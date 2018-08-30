# -*- coding:utf-8 -*-

# 把字符串转换成整数
# 将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。


class Solution:
    def str_2_int(self, string):  # 将符合规范的数字字符串转为数字
        if string == "":
            return 0
        if len(string) == 1:
            if 48 < ord(string) <= 57:
                return ord(string) - 48
            else:
                return 0
        else:  # 字符串长度大于 1
            num = 0
            if 48 < ord(string[0]) <= 57:
                num = ord(string[0])-48
                posi = 1
            elif string[0] == "-":
                if string[1] == "0":
                    return 0
                posi = -1
            elif string[0] == "+":
                posi = 1
            else:
                return 0
            for i in xrange(1, len(string)):
                if 48 <= ord(string[i]) <= 57:
                    num = num * 10 + ord(string[i])-48
                else:
                    return 0
            return num * posi


s = Solution()
print s.str_2_int('+100')
