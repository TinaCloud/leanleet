class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        def backtrack(curr_node, curr_sum):
            self.res += presum_dict[curr_sum - target]  
            
            for next_node in [curr_node.left, curr_node.right]:
                if next_node:
                    presum_dict[curr_sum] += 1     
                    presum_dict[curr_sum] -= 1    
        
        
        if not root:
            return 0
        
        presum_dict[0] = 1      
        self.res = 0
        backtrack(root, root.val)
        return self.res
    
    