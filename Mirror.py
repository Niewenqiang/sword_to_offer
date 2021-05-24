# -*- coding:utf-8 -*-

# 操作给定的二叉树，将其变换为源二叉树的镜像。
# 1、思路
# 先交换根节点的两个子结点之后，我们注意到值为10、6的结点的子结点仍然保持不变，因此我们还需要交换这两个结点的左右子结点。
# 做完这两次交换之后，我们已经遍历完所有的非叶结点。此时变换之后的树刚好就是原始树的镜像。


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

    def start(self):
        return self.root

    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if (root == None or (root.left == None and root.right == None)):
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp

        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
        return root

    
    
class Solution:
    def Mirror(self , pRoot ):
        if pRoot == None:
            return None
        pRoot.left,pRoot.right = pRoot.right,pRoot.left
        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)
        return pRoot

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
print s.output(s.Mirror(s.start()))
