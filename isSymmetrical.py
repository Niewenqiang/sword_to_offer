# -*- coding:utf-8 -*-

# 对称的二叉树

# 请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

# 解决办法就是采用前序遍历，同时考虑NULL指针。

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

    def isSymmetrical(self, pRoot):
        # write code here
        def isSame(p1, p2):
            if not p1 and not p2:
                return True
            if (p1 and p2) and p1.val == p2.val:
                return isSame(p1.left, p2.right) and isSame(p1.right, p2.left)
            return False
        if not pRoot:
            return True
        if not pRoot.left and pRoot.right:
            return False
        if not pRoot.right and pRoot.left:
            return False
        return isSame(pRoot.right, pRoot.left)


s = Solution()
s.add(0)
s.add(1)
s.add(1)
s.add(3)
s.add(4)
s.add(4)
s.add(3)
print s.PrintFromTopToBottom(s.start())
print s.isSymmetrical(s.start())
