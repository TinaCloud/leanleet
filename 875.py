class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        start, end = 1, max(piles) + 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.finish(piles, mid, H):
                end = mid
            else:
                start = mid
        return start if self.finish(piles, start, H) else end
    
    def finish(self, piles, k, H):    
        time_needed = 0
        for pile in piles:
            time_needed += (pile - 1) // k + 1
        return time_needed <= H