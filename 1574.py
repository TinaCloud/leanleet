class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        n = len(arr)
        left, right = 0, n - 1

        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        ans = min(n - left - 1, right)
        if ans == 0:
            return 0

        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1

        return ans