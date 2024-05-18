class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def recursive(root, parent):
            if not root:
                return 0
            
            moves = recursive(root.left, root) + recursive(root.right, root)
            x = root.val - 1

            if parent:
                parent.val += x
                moves += abs(x)
            return moves
        
        res = recursive(root, None)

        return res