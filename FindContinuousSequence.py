# -*- coding:utf-8 -*-


# 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
# 但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
# 没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
import math


class Solution:
    def FindContinuousSequence(self, tsum):
        res = []

        for div in range(2, int(math.sqrt(tsum * 2)) + 1):
            if (div % 2 == 0 and tsum % div == div / 2) or (div % 2 == 1 and tsum % div == 0):
                start = tsum // div - div // 2 + 1 if div % 2 == 0 else tsum // div - div // 2
                res.append(list(range(start, tsum // div + div // 2 + 1)))

        return sorted(res)


s = Solution()
print s.FindContinuousSequence(100)



import math
class Solution:
    def FindContinuousSequence(self, tsum):
        res = []
        for i in range(2, int(math.sqrt(2 * tsum)) + 1):
            if i % 2 == 1 and tsum % i == 0 and tsum // i - i // 2 > 0:
                res.append([i for i in range(tsum // i - i // 2, tsum // i + i // 2 + 1)])
            if i % 2 == 0 and tsum % i == i // 2 and tsum // i - i // 2 + 1 > 0:
                res.append([i for i in range(tsum // i - i // 2 + 1, tsum // i + i // 2 + 1)])
        return sorted(res)

    
#思路
# 首先确定遍历范围，其中X满足条件：(1+X)X = 200
# 然后根据x是奇还是偶确定list里面的数
