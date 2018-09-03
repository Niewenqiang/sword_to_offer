# -*- coding:utf-8 -*-

# 序列化二叉树
# 请实现两个函数，分别用来序列化和反序列化二叉树。

# 这道题思路简单，使用前序遍历来序列化和发序列化即可。只要自己写的程序格式对应上即可。可以使用$符号表示NULL，
# 同时每个结点之间，需要添加逗号，即','进行分隔。
#
# 直接看代码即可。


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

    def Serialize(self, root):
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        list = s.split(',')
        return self.deserializeTree(list)

    def deserializeTree(self, list):
        if len(list) <= 0:
            return None
        val = list.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.deserializeTree(list)
            root.right = self.deserializeTree(list)
        return root


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
print s.Serialize(s.start())
print s.PrintFromTopToBottom(s.Deserialize(s.Serialize(s.start())))
