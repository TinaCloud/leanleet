class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        tot = 0
        for cus, gru in zip(customers, grumpy):
            if gru == 0:
                tot += cus

        cur, n = 0, len(customers)
        for i in range(min(X, n)):
            cur += customers[i] * grumpy[i]

        increase = cur
        for i in range(X, n):
            cur += customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
            increase = max(increase, cur)

        return tot + increase