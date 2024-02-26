class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def recursive(root1, root2):
            if root1 == None and root2 != None or root1 != None and root2 == None:
                return False
            if root1 == None and root2 == None:
                return True

            return root1.val == root2.val and recursive(root1.left, root2.left) and recursive(root1.right, root2.right)
        
        return recursive(p, q)