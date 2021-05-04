class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(curr_node):
            if not curr_node:
                return
            for next_node in [curr_node.left, curr_node.right]:
                if next_node:
                    graph[curr_node].append(next_node)
                    graph[next_node].append(curr_node)
                    dfs(next_node)
                    
                    
        def dfs2(curr_node, curr_dist):
            if curr_dist == K:
                res.append(curr_node.val)
                return
            for next_node in graph[curr_node]:
                if next_node not in visited:
                    visited.add(next_node)
                    dfs2(next_node, curr_dist + 1)
            
            
        graph = defaultdict(list)
        dfs(root)    
        res = []
        visited = set()
        for node in graph:
            if node == target:
                visited.add(node)
                dfs2(node, 0)
        return res
    
    