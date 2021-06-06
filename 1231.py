class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def check(x):
            s = 0
            count = 0
            for num in sweetness:
                s += num
                if s >= x:
                    count += 1
                    s = 0
            return count >= K + 1

        l, r = 0, sum(sweetness) // (K + 1)
        while l < r:
            mid = l + (r - l + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l






    