class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return res.largest

    def dfs(self, root):
        if not root:
            return SubTree(0, 0, float('inf'), float('-inf'))

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if root.val > left.max and root.val < right.min:
            size = left.size + right.size + 1
        else:
            size = float('-inf')

        largest = max(left.largest, right.largest, size)

        return SubTree(largest, size, min(root.val, left.min), max(root.val, right.max))

