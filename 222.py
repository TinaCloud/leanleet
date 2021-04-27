class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        
        if left_depth == right_depth:   
            return 2**left_depth + self.countNodes(root.right)
        elif left_depth > right_depth: 
            return 2**right_depth + self.countNodes(root.left)
        
    def depth(self, root): 
        if not root:
            return 0
        
        return max(self.depth(root.left), self.depth(root.right)) + 1
