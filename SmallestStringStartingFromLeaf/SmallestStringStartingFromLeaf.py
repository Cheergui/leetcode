import string

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """

        root = TreeNode(val=root.val, parent=None, left=root.left, right=root.right)

        alphabet = string.ascii_lowercase

        hashmap1 = {letter:[] for letter in alphabet}

        def letter_to_number(letter):
            return ord(letter) - ord('a')

        def recursive(root):
            if not root.left and not root.right:
                letter = alphabet[root.val]
                hashmap1[letter].append(['', root])
            
            if root.left:
                newLeft = TreeNode(val=root.left.val, parent=root, left=root.left.left, right=root.left.right)
                recursive(newLeft)
            if root.right:
                newRight = TreeNode(val=root.right.val, parent=root, left=root.right.left, right=root.right.right)
                recursive(newRight)

        recursive(root)

        hashmap2 = None

        sequence_res, node_res = None, None

        loop = True

        while loop:
            if hashmap2 != None:
                hashmap1 = hashmap2
            hashmap2 = {letter:[] for letter in alphabet}
            for letter in alphabet:
                if len(hashmap1[letter]) > 0:
                    if len(hashmap1[letter]) == 1:
                        sequence_res, node_res = hashmap1[letter][0]
                        loop = False
                        break
                    else:
                        for sequence, node in hashmap1[letter]:
                            if node == None:
                                sequence_res, node_res = sequence, node
                                loop = False
                                break
                            new_letter = alphabet[node.val]
                            new_sequence = sequence + new_letter
                            hashmap2[new_letter].append([new_sequence, node.parent])
                        break
        
        while node_res != None:
            new_letter = alphabet[node_res.val]
            sequence_res = sequence_res + new_letter
            node_res = node_res.parent

        return sequence_res