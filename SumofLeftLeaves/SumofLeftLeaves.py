class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def recursive(root, state):
            if not root or not root.left and not root.right and state == 'right':
                return 0
            if not root.left and not root.right and state == 'left':
                return root.val
            
            return recursive(root.left, 'left') + recursive(root.right, 'right')
        
        res = recursive(root, 'right')

        return res 