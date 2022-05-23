# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        if node is None:
            return
        
        # lrn - postorder traversal
        left = self.invertTree(node.left)
        right = self.invertTree(node.right)
        node.right, node.left = left, right
        return node

    # nlr - PreOrder traversal or DSF
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        node = root
        if node is None:
            return 0
        
        max_left = maxDepth(node.left)
        max_right = maxDepth(node.right)
        # include current node in the count +1
        return max(max_left, max_right) + 1
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        if p.value != q.value:
            return False
        
        return (self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right))