class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l = 1
        r = MAX = 10000001
        
        while l < r:
            mid = (l + r) // 2
            tmp = sum((x + mid - 1) // mid for x in dist[:-1]) + dist[-1] / mid
            if tmp <= hour:
                r = mid
            else:
                l = mid + 1
        
        return l if l < MAX else -1









    