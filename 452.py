class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[1], x[0]))
        
        min_end = -sys.maxsize
        shots = 0
        for start, end in points:
            if start <= min_end:
                min_end = min(min_end, end)
            else:
                shots += 1
                min_end = end
        return shots