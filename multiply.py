# -*- coding:utf-8 -*-

# 构建乘积数组

# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

# 观察下公式，你会发现，B[i]公式中没有A[i]项，也就是说如果可以使用除法，就可以用公式B[i]=A[0]*A[1]*.....*A[n-1]/A[i]来计算B[i]，
# 但是题目要求不能使用，因此我们只能另想办法。
#
# 现在要求不能使用除法，只能用其他方法。一个直观的解法是用连乘n-1个数字得到B[i]。显然这个方法需要O(n*n)的时间复杂度。
#
# 好在还有更高效的算法。可以把B[i]=A[0]*A[1]*.....*A[i-1]*A[i+1]*.....*A[n-1]。看成A[0]*A[1]*.....*A[i-1]和
# A[i+1]*.....A[n-2]*A[n-1]两部分的乘积。

# 不妨设定C[i]=A[0]*A[1]*...*A[i-1]，D[i]=A[i+1]*...*A[n-2]*A[n-1]。C[i]可以用自上而下的顺序计算出来，即C[i]=C[i-1]*A[i-1]。
# 类似的，D[i]可以用自下而上的顺序计算出来，即D[i]=D[i+1]*A[i+1]。


class Solution:
    def multiply(self, A):
        # write code here
        if A is None or len(A) == 0:
            return []

        B = [1] * len(A)
        for i in range(1, len(A)):
            B[i] = B[i - 1] * A[i - 1]

        tmp = 1
        for i in range(len(A) - 2, -1, -1):
            tmp *= A[i + 1]
            B[i] *= tmp

        return B


s = Solution()
print s.multiply([2, 3, 4, 5, 6, 7])
