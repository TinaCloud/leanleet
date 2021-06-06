class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        for x in range(0, n + 1):       #x个元素
            idx = bisect.bisect_left(nums, x)
            cur_cnt = n-1 - idx + 1     #大于等于x的个数

            if cur_cnt == x:
                return x
        return -1










    