class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ca = Counter(map(lambda x: x * x, na))
        cb = Counter(map(lambda x: x * x, nb))
        res = 0
        for i, n in enumerate(na):
            res += sum(map(lambda j: cb[n * na[j]], range(i + 1, len(na))))
        for i, n in enumerate(nb):
            res += sum(map(lambda j: ca[n * nb[j]], range(i + 1, len(nb))))
        return res
