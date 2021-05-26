# 给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），
# 每段绳子的长度记为k[1],...,k[m]。请问k[1]x...xk[m]可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。


# 动态规划算法

# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        result = [0,1,2,3]
        for i in range (4,number+1):
            max = 0
            for j in range(1,i//2 +1):
                res = result[j] * result[i-j]
                if res > max:
                    max = res
            result.append(max)
        return result[-1]
