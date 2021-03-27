class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort()
        l, r = 0, len(nums) - 1
        res, MOD = 0, 10**9 + 7

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, MOD)
                l += 1

        return res % MOD