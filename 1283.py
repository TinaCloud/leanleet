class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        compute_sum = lambda x : sum([ceil(n / x) for n in nums])

        left, right = 1, nums[-1]
        while left <= right:
            pivot = (right + left) >> 1
            num = compute_sum(pivot)

            if num > threshold:
                left = pivot + 1
            else:
                right = pivot - 1

        return left
    