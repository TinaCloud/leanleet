class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        n = len(inventory)
        count = 0
        index = n
        for i in range(n-1):
            diff = inventory[i] - inventory[i+1]
            count += diff * (i + 1)
            if count >= orders:
                index = i + 1
                break
        total = sum(inventory[:index])
        mean = (total - orders) // index
        remainder = (total - orders) % index
        ans = 0
        cons = 10 ** 9 + 7
        for i in range(index):
            ans += (inventory[i] + mean + 1) * (inventory[i] - mean)//2
            ans %= cons
        ans -= (mean + 1) * remainder
        ans %= cons
        return ans









    