class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        sums = 0
        max_len = -1
        j = 0
        for i, num in enumerate(nums):
            while j < len(nums) and sums < target:
                sums += nums[j]
                j += 1

            if sums == target:
                max_len = max(max_len, j - i)
                
            sums -= num
            
        return len(nums) - max_len if max_len != -1 else -1




    