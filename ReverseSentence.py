# -*- coding:utf-8 -*-

# 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，
# 有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，
# 这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，
# 你能帮助他么？
# 1、思路
#
# 观察字符串变化规律，你会发现这道题很简单。只需要对每个单词做翻转，然后再整体做翻转就得到了正确的结果。


# class Solution:
#     def ReverseSentence(self, s):
#         # write code here
#         if s is None or len(s) == 0:
#             return s
#         stack = []
#         for i in s.split(' '):
#             stack.append(i)
#         ans = ""
#         while len(stack) > 0:
#             ans += stack.pop() + " "
#         ans = ans[:-1]
#         return ans


class Solution:
    def ReverseSentence(self, sentence):
        if sentence is None or len(sentence) == 0:
            return sentence
        return ' '.join(sentence.split(' ')[::-1])


s = Solution()
print s.ReverseSentence('student. a am I')
