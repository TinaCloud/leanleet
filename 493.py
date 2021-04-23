class SegmentTree:
    
    def __init__(self, start, end, cnt):
        self.start = start
        self.end = end
        self.cnt = cnt
        self.left = None
        self.right = None
        
    def build(self, start, end):
        if start > end:
            return
        
        root = SegmentTree(start, end, 0)
        if start == end:
            return root
        
        mid = start + (end - start) // 2
        root.left = self.build(start, mid)
        root.right = self.build(mid+1, end)
        root.cnt = 0
        
        return root
    
    def update(self, root, num):
        if root.start > num or root.end < num:
            return
        
        if root.start == root.end:
            root.cnt += 1
            return
        
        mid = root.start + (root.end - root.start) // 2
        if num <= mid:
            self.update(root.left, num)
        else:
            self.update(root.right, num)
            
        root.cnt = root.left.cnt + root.right.cnt
        
    def query(self, root, start, end):
        if start > root.end or end < root.start:
            return 0
        
        elif start <= root.start and end >= root.end:
            return root.cnt
        
        else:
            return self.query(root.left, start, end) + self.query(root.right, start, end)


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        
        lens = len(nums)
        min_num, max_num = min(nums), max(nums)
        segment_tree = SegmentTree(min_num, max_num, 0)
        root = segment_tree.build(min_num, max_num)
        
        res = 0
        for i in range(1, len(nums)):
            segment_tree.update(root, nums[i-1])
            res += segment_tree.query(root, 2*nums[i]+1, max_num)   
        return res
