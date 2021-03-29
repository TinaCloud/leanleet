class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        currMinimum = nums[k]
        currBest = currMinimum
        n = len(nums)
        nums += [-1]
        left, right = k - 1, k + 1
        while True:

            while nums[left] >= currMinimum:
                left -= 1
            while nums[right] >= currMinimum:
                right += 1

            currBest = max(currBest, currMinimum * (right - left - 1))

            if left < 0 or right > n - 1:
                break

            if nums[left] >= nums[right]:
                currMinimum = nums[left]
                left -= 1
            else:
                currMinimum = nums[right]
                right += 1

        while left >= 0:
            currMinimum = min(currMinimum, nums[left])
            left -= 1
            currBest = max(currBest, currMinimum * (right - left - 1))

        while right < n:
            currMinimum = min(currMinimum, nums[right])
            right += 1
            currBest = max(currBest, currMinimum * (right - left - 1))

        return max(currBest, currMinimum * n)