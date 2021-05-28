# -*- coding:utf-8 -*-

# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
# 但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
# 1、思路
#
# 借用一个辅助的栈，遍历压栈顺序，先讲第一个放入栈中，这里是1，然后判断栈顶元素是不是出栈顺序的第一个元素，
# 这里是4，很显然1≠4，所以我们继续压栈，直到相等以后开始出栈，出栈一个元素，则将出栈顺序向后移动一位，直到不相等，
# 这样循环等压栈顺序遍历完成，如果辅助栈还不为空，说明弹出序列不是该栈的弹出顺序。


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(popV) == 0 or len(pushV) != len(popV):
            return False
        stackData = []
        for i in pushV:
            stackData.append(i)
            while len(stackData) and stackData[-1] == popV[0]:
                stackData.pop()
                popV.pop(0)
        if len(stackData):
            return False
        return True


s = Solution()
print s.IsPopOrder([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
print s.IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])


class Solution:
    def IsPopOrder(self, pushV, popV):
        tmp = []
        for i in pushV:
            tmp.append(i)
            while len(tmp) > 0 and tmp[-1] == popV[0]:
                tmp.pop()
                popV.pop(0)
        return len(tmp) == 0
    
    
