from collections import deque

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        queue = deque()
        queue.append(root)

        while queue:
            line = []
            for i in range(len(queue)):
                node = queue.popleft()
                line.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        
        return line[0]