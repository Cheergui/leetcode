# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        res = [0]


        def recursive(root, string):
            if not root:
                return
            if not root.left and not root.right:
                string += str(root.val)
                res[0] += int(string)

            recursive(root.left, string + str(root.val))
            recursive(root.right, string + str(root.val))

        recursive(root, '')

        return res[0]