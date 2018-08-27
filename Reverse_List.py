# -*- coding:utf-8 -*-

# 输入一个链表，反转链表后，输出链表的所有元素。
# 1、思路
#
# 这个很简单，我们使用三个指针，分别指向当前遍历到的结点、它的前一个结点以及后一个结点。
#
# 在遍历的时候，做当前结点的尾结点和前一个结点的替换。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

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

    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        last = None
        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last

s = Solution()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.append(6)
print s.ReverseList(s.start()).next.next.val
print s.start().val