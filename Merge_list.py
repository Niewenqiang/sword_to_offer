# -*- coding:utf-8 -*-

# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
# 1、思路
#
# 先判断输入的链表是否为空的指针。如果第一个链表为空，则直接返回第二个链表；如果第二个链表为空，则直接返回第一个链表。
# 如果两个链表都是空链表，合并的结果是得到一个空链表。
#
# 两个链表都是排序好的，我们只需要从头遍历链表，判断当前指针，哪个链表中的值小，即赋给合并链表指针即可。使用递归就可以轻松实现。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表

    # 链表初始化
    def __init__(self, node=None):
        self.__head = node

    # 链表插值
    def append(self, item):
        node = ListNode(item)
        if self.__head == None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    # 链表的初始位置
    def start(self):
        return self.__head


    def Merge(self, pHead1, pHead2):

        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        pMergeHead = None
        if pHead1.val < pHead2.val:
            pMergeHead = pHead1
            pMergeHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergeHead = pHead2
            pMergeHead.next = self.Merge(pHead1, pHead2.next)
        return pMergeHead

s = Solution()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.append(6)
t = Solution()
t.append(7)
t.append(8)
t.append(9)

print s.Merge(s.start(), t.start()).next.next.next.next.next.next.val