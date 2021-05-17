# -*- coding:utf-8 -*-

# 输入两个链表，找出它们的第一个公共结点。
# 方法一：
# 我们可以把两个链表拼接起来，一个pHead1在前pHead2在后，一个pHead2在前pHead1在后。这样，生成了两个相同长度的链表，
# 那么我们只要同时遍历这两个表，就一定能找到公共结点。时间复杂度O(m+n)，空间复杂度O(m+n)。
#
# 方法二：
# 我们也可以先让把长的链表的头砍掉，让两个链表长度相同，这样，同时遍历也能找到公共结点。
# 此时，时间复杂度O(m+n)，空间复杂度为O(MAX(m,n))。

# https://blog.csdn.net/qq_36243414/article/details/90452723


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


    def intersect(self, pHead1, pHead2, item):
        node = ListNode(item)
        cur1 = pHead1
        if pHead1 == None:
            self.__head = node
        else:
            while cur1.next != None:
                cur1 = cur1.next
            cur1.next = node
        cur2 = pHead2
        if pHead2 == None:
            self.__head = node
        else:
            while cur2.next != None:
                cur2 = cur2.next
            cur2.next = node


    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        cur1, cur2 = pHead1, pHead2
        while cur1 != cur2:
            cur1 = cur1.next if cur1 != None else pHead2
            cur2 = cur2.next if cur2 != None else pHead1
        return cur1


s = Solution()
s.append(1)
s.append(6)
t = Solution()
t.append(7)
t.append(8)
t.append(9)
s.intersect(s.start(), t.start(), 10)
t.append(11)


print s.FindFirstCommonNode(s.start(), t.start()).val
print s.start().next.next.next.val
