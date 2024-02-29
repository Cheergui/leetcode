from collections import deque

class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        queue = deque()
        queue.append(root)

        level = 0

        while queue:
            if level % 2 == 0:
                tmp = [float('-inf')]
            if level % 2 == 1:
                tmp = [float('inf')]
            for i in range(len(queue)):
                node = queue.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0 or node.val <= tmp[-1]:
                        return False
                if level % 2 == 1:
                    if node.val % 2 == 1 or node.val >= tmp[-1]:
                        return False
                tmp.append(node.val)    
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            level += 1

        return True