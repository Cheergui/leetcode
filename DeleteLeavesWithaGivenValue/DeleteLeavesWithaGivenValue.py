class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """

        def recursive(root, target):
            if root:
                root.left = recursive(root.left, target)
                root.right = recursive(root.right, target)
                if not root.left and not root.right and root.val == target:
                    return None
                return root
        
        if root:
            return recursive(root, target)
        
        return None