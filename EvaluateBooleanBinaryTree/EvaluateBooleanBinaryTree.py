class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def recursive(root):
            if not root.left and not root.right:
                return bool(root.val)

            if root.val == 2:
                return recursive(root.left) or recursive(root.right)

            if root.val == 3:
                return recursive(root.left) and recursive(root.right)

        res = recursive(root)

        return res