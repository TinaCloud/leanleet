class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return - 1

        def count(day):
            curr_flower = total_bouquet = 0
            for day1 in bloomDay:
                if day1 <= day:
                    curr_flower += 1
                else:
                    total_bouquet += curr_flower // k
                    curr_flower = 0
            total_bouquet += curr_flower // k
            return total_bouquet >= m
        

        left, right = min(bloomDay), max(bloomDay)     
        while left < right:
            mid = left + (right - left >> 2)
            if count(mid):
                right = mid
            else:
                left = mid + 1
        return left