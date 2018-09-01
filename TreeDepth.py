# -*- coding:utf-8 -*-

# 二叉树的深度

# 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
# 1、思路
#
# 这道题蛮简单的，求二叉树的深度。可以是递归的方法，属于DFS（深度优先搜索）；另一种方法是按照层次遍历，属于BFS（广度优先搜索）。


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

    def maxDepth(self, root):
        if not root:  # 递归边界
            return 0
        else:
            l = 1 + self.maxDepth(root.left)  # 递归
            r = 1 + self.maxDepth(root.right)
            return max(l, r)


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
print s.maxDepth(s.start())
