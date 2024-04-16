from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """

        if depth == 1:
            newRoot = TreeNode(val=val)
            newRoot.left = root
            return newRoot
        
        queue = deque()
        queue.append(root)

        currDepth = 1

        while queue:
            if currDepth != depth-1:
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                currDepth += 1
            else:
                for i in range(len(queue)):
                    node = queue.popleft()
                    
                    # Accessing the old left and right children
                    oldLeft = node.left
                    oldRight = node.right

                    # Creating the new left and right children
                    newLeft = TreeNode(val=val)
                    newRight = TreeNode(val=val)

                    # Assigning the new left and right childs as the node's children
                    node.left = newLeft
                    node.right = newRight

                    # Assigning the old left and right childs as the new nodes' children
                    newLeft.left = oldLeft
                    newRight.right = oldRight

        return root