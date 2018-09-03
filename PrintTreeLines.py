# -*- coding:utf-8 -*-

# 把二叉树打印成多行

# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
# 思路和上一道题一样，区别在于，这把是先入先出，使用队列即可。


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

    def Print(self, pRoot):
        if not pRoot:
            return []
        resultList = []
        curLayer = [pRoot]
        while curLayer:
            curList = []
            nextLayer = []
            for node in curLayer:
                curList.append(node.val)
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
            resultList.append(curList)
            curLayer = nextLayer
        return resultList


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
print s.Print(s.start())
