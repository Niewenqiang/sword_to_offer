# -*- coding:utf-8 -*-


# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.root = None

    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            pos = tin.index(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:1+pos], tin[:pos])
            root.right = self.reConstructBinaryTree(pre[1+pos:], tin[pos+1:])
        return root

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

    def output(self, root):
        if root is None:
            return
        queue = [root]
        while queue:
            curr = queue.pop(0)
            print curr.val
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)


s = Solution()
print s.output(s.reConstructBinaryTree([0, 1, 3, 7, 8, 4, 9, 2, 5, 6], [7, 3, 8, 1, 9, 4, 0, 5, 2, 6]))



