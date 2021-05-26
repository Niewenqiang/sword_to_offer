# -*- coding:utf-8 -*-


# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
# 大家首先想到的是顺序扫描法，但是这种方法的时间复杂度是O（n^2）。接着大家又会考虑用哈希表的方法，但是空间复杂度不是O（1）。
# 应该怎么做才能即满足时间复杂度是O（n）又满足空间复杂度是O（1）的要求呢？
# 我们可以想一想“异或”运算的一个性质，我们直接举例说明。
# 我们知道异或的一个性质是：任何一个数字异或它自己都等于0。也就是说，如果我们从头到尾依次异或数组中的每一个数字，
# 那么最终的结果刚好是那个只出现一次的数字。


# class Solution:
#     # 返回[a,b] 其中ab是出现一次的两个数字
#     def FindNumsAppearOnce(self, array):
#         # write code here
#         tagdict={}
#         for i in array:
#             if i in tagdict:
#                 tagdict[i]+=1
#             else:
#                 tagdict[i]=1
#         taglist=[]
#         for j in tagdict:
#             if tagdict[j]==1:
#                 taglist.append(j)
#         return taglist
#
# s = Solution()
# print s.FindNumsAppearOnce([1, 2, 2])

# class Solution:
#     def singleNumber(self, nums):
#         res = 0
#         for i in nums:
#             res ^= i
#         return res


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        xor = 0
        for i in array:
            xor ^= i
        num1, num2 = 0, 0
        mask = 1
        while xor & mask == 0:
            mask <<= 1
        for num in array:
            if num & mask == 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]


s = Solution()
print s.FindNumsAppearOnce([1, 2, 3, 4, 2, 4])

#思路
# 要确定两个数字，首先全部异或，获取到两个数字的异或值，然后依次判断哪个位为1，该位为1则说明这两个数在该位不同。
# 通过这个为1的位，将数组中的数字分为两个组，这两个数肯定在不同的组内，然后组内各自异或就能得到答案。

