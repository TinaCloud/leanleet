class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(start, end):
            if start >= end:
                return None
            
            root = TreeNode(postorder[self.post_idx])
            self.post_idx -= 1
            idx = num_idx[root.val]
            
            root.right = build(idx + 1, end)       
            root.left = build(start, idx)        
        
            return root
        
        
        num_idx = defaultdict(int)
        for idx, num in enumerate(inorder): 
            num_idx[num] = idx
            
        self.post_idx = len(postorder) - 1
        return build(0, len(inorder))
    