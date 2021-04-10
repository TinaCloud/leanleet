class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1 for _ in range(n)] for _ in range(n)]
        
        def combine(x, y):
            if x == 0 or y == 0: return 1
            if memo[x][y] != -1: return memo[x][y]
            memo[x][y] = combine(x, y - 1) + combine(x - 1, y)
            return memo[x][y]
        
        def f(nums):
            if len(nums) <= 2: return 1
            left, right = [], []
            for i in range(1, len(nums)):
                if nums[i] < nums[0]: left.append(nums[i])
                if nums[i] > nums[0]: right.append(nums[i])
            cnt = combine(len(left), len(right))
            return cnt * f(left) * f(right)
        
        return (f(nums)-1) % (10**9+7)

    