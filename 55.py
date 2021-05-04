class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)    
        dp[0] = True                
        for j in range(1, len(nums)):
            for i in range(j):
                if dp[i] and i + nums[i] >= j:  
                    dp[j] = True
                    break
        
        return dp[-1]
