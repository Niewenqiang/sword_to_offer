# -*- coding:utf-8 -*-

# 输入一个链表，返回一个反序的链表。
# 1、思路
# 通常，这种情况下，我们不希望修改原链表的结构。返回一个反序的链表，这就是经典的“后进先出”，我们可以使用栈实现这种顺序。
# 每经过一个结点的时候，把该结点放到一个栈中。当遍历完整个链表后，再从栈顶开始逐个输出结点的值，给一个新的链表结构，这样链表就实现了反转。
# 对于python来讲，不用如此麻烦，我们可以直接使用列表的插入方法，每次插入数据，只插入在首位。

# 链表节点
class ListNode(object):
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

    def printListFromTailToHead(self, listNode):
        result = []
        while listNode:
            result.insert(0, listNode.val)
            listNode = listNode.next
        return result


s = Solution()
s.append(1)
s.append(2)
s.append(3)
print s.printListFromTailToHead(s.start())
