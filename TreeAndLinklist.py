# -*- coding:utf-8 -*-

# 二叉搜索树与双向链表

# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.root = None

    def add(self, x):
        node = TreeNode(x)
        if self.root is None:
            self.root = node
            return
        tree = [self.root]
        while tree:
            curr = tree.pop(0)
            if curr.left is None:
                curr.left = node
                return
            else:
                tree.append(curr.left)
            if curr.right is None:
                curr.right = node
                return
            else:
                tree.append(curr.right)

    def start(self):
        return self.root

    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        result = []
        tmp = [root]
        while len(tmp):
            cur = tmp.pop(0)
            result.append(cur.val)
            if cur.left:
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)
        return result

    def Convert(self, pRootOfTree):
        self.linkedlistLast = None
        self.convertNode(pRootOfTree)
        pHead = self.linkedlistLast
        while pHead and pHead.left:
            pHead = pHead.left
        return pHead

    def convertNode(self, root):
        if not root:
            return
        pcurr = root
        if pcurr.left:
            self.convertNode(pcurr.left)
        pcurr.left = self.linkedlistLast
        if self.linkedlistLast:
            self.linkedlistLast.right = pcurr
        self.linkedlistLast = pcurr

        if pcurr.right:
            self.convertNode(pcurr.right)

    def printList(self, listNode):
        result = []
        while listNode:
            result.append(listNode.val)
            listNode = listNode.right
        return result


s = Solution()
s.add(0)
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(6)
s.add(7)
s.add(8)
print s.PrintFromTopToBottom(s.start())
print s.printList(s.Convert(s.start()))
