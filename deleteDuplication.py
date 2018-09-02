# -*- coding:utf-8 -*-


# 删除链表中重复的结点

# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5。
# 1、思路
#
# 删除重复结点，只需要记录当前结点前的最晚访问过的不重复结点pPre、当前结点pCur、指向当前结点后面的结点pNext的三个指针即可。
# 如果当前节点和它后面的几个结点数值相同，那么这些结点都要被剔除，然后更新pPre和pCur；如果不相同，则直接更新pPre和pCur。
#
# 需要考虑的是，如果第一个结点是重复结点我们该怎么办？这里我们分别处理一下就好，如果第一个结点是重复结点，那么就把头指针pHead也更新一下。


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

    def printLinklist(self, pHead):
        if pHead is None:
            return []
        cur = pHead
        result = []
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

    def deleteDuplication(self, pHead):
        first = ListNode(-1)
        first.next = pHead
        curr = pHead
        last = first
        while curr and curr.next:
            if curr.val != curr.next.val:
                curr = curr.next
                last = last.next
            else:
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
                last.next = curr
        return first.next


s = Solution()
s.append(1)
s.append(1)
s.append(2)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.append(6)
print s.printLinklist(s.start())
print s.printLinklist(s.deleteDuplication(s.start()))
