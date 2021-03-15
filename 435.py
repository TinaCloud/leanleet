class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()       
        
        min_end = -sys.maxsize
        remove_cnt = 0
        for start, end in intervals:
            if start >= min_end:
                min_end = end
                
            else:    
                remove_cnt += 1
                min_end = min(min_end, end) 
                
        return remove_cnt










































