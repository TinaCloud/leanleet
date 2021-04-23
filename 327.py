class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presums = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            presums[i+1] = presums[i] + nums[i]
        
        presum_dict = collections.defaultdict(int)  
        cnt = 0
        for presum in presums:
            for target in range(lower, upper + 1):
                cnt += presum_dict[presum - target]
            presum_dict[presum] += 1
            
        return cnt

    