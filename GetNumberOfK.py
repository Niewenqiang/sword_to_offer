# -*- coding:utf-8 -*-

# 数字在排序数组中出现的次数


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)


s = Solution()
print s.GetNumberOfK([1, 2, 3, 4, 5, 3], 3)



# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if len(data) < 1:
            return 0
        mid = len(data)//2
        if data[mid] == k:
            start,end =mid,mid
            for i in range(mid-1,-1,-1):
                if data[i] == k:
                    start = i
            for i in range(mid+1,len(data)):
                if data[i] == k:
                    end = i
            return end-start+1
        elif data[mid] < k:
            return self.GetNumberOfK(data[mid+1:],k)
        else:
            return self.GetNumberOfK(data[:mid],k)
        
        
        
        
