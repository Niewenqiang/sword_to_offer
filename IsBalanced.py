# -*- coding:utf-8 -*-

# 平衡二叉树

# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
# 1、思路
#
# 平衡二叉树的定义是：所谓的平衡之意，就是树中任意一个结点下左右两个子树的高度差不超过 1。
#
# 解题思路有两种，只遍历一次的方法最优。
#
# 重复遍历多次：
#
# 在遍历树的每个结点的时候，调用函数TreeDepth得到它的左右子树的深度。如果每个结点的左右子树的深度相差都不超过1，则这是一颗平衡的二叉树。
# 这种方法的缺点是，首先判断根结点是不是平衡的，需要使用TreeDepth获得左右子树的深度，然后还需要继续判断子树是不是平衡的，
# 还是需要使用TreeDepth获得子树的左右子树的深度，这样就导致了大量的重复遍历。
#
# 只遍历一次：
#
# 重复遍历会影响算法的性能，所以很有必要掌握不需要重复遍历的方法。如果我们用后序遍历的方式遍历二叉树的每一个结点，
# 在遍历到一个结点之前我们就已经遍历了它的左右子树。只要在遍历每个结点的时候记录它的深度（某一结点的深度等于它到叶结点的路径的长度），
# 我们就可以一边遍历一边判断每个结点是不是平衡的。


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

    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if abs(left - right) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left, right) + 1


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
print s.IsBalanced_Solution(s.start())
