# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def merge(t1,t2):
	"""
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
    if not t1:
    	return t2
    if not t2:
    	return t1

    t1.val += t2.val
    t1.left = merge(t1.left,t2.left)
    t2.right = merge(t1.right,t2.right)
    r
    eturn t1
    