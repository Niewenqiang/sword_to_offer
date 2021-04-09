# -*- coding:utf-8 -*-

# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
# 1、思路
#
# 遇到这个题，全排列当然可以做，但是时间复杂度为O(n!)。在这里我们自己定义一个规则，对拼接后的字符串进行比较。
#
# 排序规则如下：
#
#     若ab > ba 则 a 大于 b，
#     若ab < ba 则 a 小于 b，
#     若ab = ba 则 a 等于 b；
#
# 根据上述规则，我们需要先将数字转换成字符串再进行比较，因为需要串起来进行比较。比较完之后，按顺序输出即可。

class Solution:
    def PrintMinNumber(self, numbers):
        if len(numbers) == 0:
            return ''
        compare = lambda a, b: cmp(str(a) + str(b), str(b) + str(a))
        min_string = sorted(numbers, cmp=compare)
        print min_string
        return ''.join(str(s) for s in min_string)


s = Solution()
print s.PrintMinNumber([3, 23, 321, 1, 2, 12])


class Solution:
    def PrintMinNumber(self, numbers):
        li = self.qsort(numbers)
        return "".join([str(i) for i in li])

    def comp(self,a,b):
        if str(a) + str(b) < str(b) + str(a):
            return True
        else:
            return False
    def qsort(self,n):
        if len(n) <= 1:
            return n
        return self.qsort([i for i in n[1:] if self.comp(i,n[0])]) + [n[0]] + self.qsort([i for i in n[1:] if not self.comp(i,n[0])])
   

