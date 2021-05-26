# -*- coding:utf-8 -*-

# 字符流中第一个不重复的字符
# 请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
# 第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
#
# 输出描述：
#     如果当前字符流没有存在出现一次的字符，返回#字符。

# 1、思路
# 这道题还是很简单的。将字节流保存起来，通过哈希表统计字符流中每个字符出现的次数，顺便将字符流保存在string中，
# 然后再遍历string，从哈希表中找到第一个出现一次的字符。


class Solution:
    def FirstAppearingOnce(self, s):
        if s is []:
            return '#'
        i = 0
        while i < len(s):
            if s[i] not in s[:i] and s[i] not in s[i+1:]:
                return s[i]
            else:
                i += 1
        return '#'


s = Solution()
print s.FirstAppearingOnce('google')


# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ""
        self.dict = {}
    def FirstAppearingOnce(self):
        for i in self.s:
            if self.dict[i] == 1:
                return i
        return '#'
    def Insert(self, char):
        self.s += char
        self.dict[char] = self.dict.get(char,0) + 1
        
        
    
    
