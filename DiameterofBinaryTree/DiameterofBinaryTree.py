class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]

        def recursive(root):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                return 1

            depth_left = recursive(root.left)
            depth_right = recursive(root.right)
            if depth_left + depth_right > res[0]:
                res[0] = depth_left + depth_right
            return max(depth_left, depth_right) + 1

        recursive(root)
        return res[0]  