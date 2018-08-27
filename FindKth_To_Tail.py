# -*- coding:utf-8 -*-

# 输入一个链表，输出该链表中倒数第k个结点。
# 1、思路
#
# 我们可以定义两个指针。第一个指针从链表的头指针开始遍历向前走k-1，第二个指针保持不动；从第k步开始，
# 第二个指针也开始从链表的头指针开始遍历。由于两个指针的距离保持在k-1，当第一个（走在前面的）指针到达链表的尾结点时，
# 第二个指针（走在后面的）指针正好是倒数第k个结点。
# 除此之外，要注意代码的鲁棒性。需要判断传入参数合法性问题。


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

    def FindKthToTail(self, head, k):
        l = []
        m = []
        while head:
            l.append(head)
            m.append(head.val)
            head = head.next
        if len(l) < k or k < 1:
            return None
        return l[-k], m[-k]


s = Solution()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.append(6)
print s.FindKthToTail(s.start(), 3)
