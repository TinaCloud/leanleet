class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start, end = max(nums), sum(nums) + 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.split(nums, m, mid):
                end = mid
            else:
                start = mid
        return start if self.split(nums, m, start) else end
    
    def split(self, nums, m, max_sum):
        cnt = 0
        i = 0
        while i < len(nums):
            curr_sum = 0
            while i < len(nums) and curr_sum + nums[i] <= max_sum:
                curr_sum += nums[i]
                i += 1
            cnt += 1
        return cnt <= m
