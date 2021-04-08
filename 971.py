class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        def dfs(root):
            if not root:
                return True
            if root.val != voyage[self.idx]:
                return False
            
            self.index += 1
            if root.left and root.left.val != voyage[self.index]:
                res.append(root.val)
                root.left, root.right = root.right, root.left
                
            return dfs(root.left) and dfs(root.right)
                        
        self.index = 0   
        res = []           
        return res if dfs(root)  else [-1]     

    