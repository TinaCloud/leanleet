class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(in_start, in_end):
            if in_start >= in_end:
                return None
            
            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1
            in_idx = num_idx[root.val]
            
            root.left = build(in_start, in_idx)
            root.right = build(in_idx + 1, in_end)
            
            return root
        
        
        num_idx = defaultdict(int)
        for idx, num in enumerate(inorder):
            num_idx[num] = idx
        
        self.pre_idx = 0
        return build(0, len(inorder))

    