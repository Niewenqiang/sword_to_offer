# -*- coding:utf-8 -*-


# 复杂链表的复制
# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
# （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

# 我们这里采用三步：
#
#     第一步：复制复杂指针的label和next。但是这次我们把复制的结点跟在元结点后面，而不是直接创建新的链表；
#     第二步：设置复制出来的结点的random。因为新旧结点是前后对应关系，所以也是一步就能找到random；
#     第三步：拆分链表。奇数是原链表，偶数是复制的链表。


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead
        cloNode = pHead
        while cloNode:
            node = RandomListNode(cloNode.label)
            node.next = cloNode.next
            cloNode.next = node
            cloNode = node.next
        cloNode = pHead
        while cloNode:
            node = cloNode.next
            if cloNode.random:
                node.random = cloNode.random.next
            cloNode = node.next
        cloNode = pHead
        pHead = pHead.next
        while cloNode.next:
            node = cloNode.next
            cloNode.next = node.next
            cloNode = node
        return pHead