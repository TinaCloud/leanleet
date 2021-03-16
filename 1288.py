class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0], -x[1]))   
        heap = []     
        remove = 0
        
        for start, end in intervals:
            if len(heap) > 0 and end <= -heap[0]:  
                remove += 1    
            heappush(heap, -end)
            
        return len(intervals) - remove