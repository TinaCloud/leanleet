class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        r_start, r_end = toBeRemoved[0], toBeRemoved[1]
        
        for start, end in intervals:
            
            if end <= r_start:
                res.append([start, end])
            elif start >= r_end:
                res.append([start, end])
                
            elif start >= r_start and end <= r_end:
                continue
            elif start < r_start and end > r_end:
                res.append([start, r_start])
                res.append([r_end, end])
                
            elif r_start < end <= r_end:
                res.append([start, r_start])
            elif r_start <= start < r_end:
                res.append([r_end, end])

        return res