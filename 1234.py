class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        counter = collections.Counter(s)   
        min_size = n
        j = 0
        for i in range(len(s)):
            while j < n and not all(cnt <= n//4 for cnt in counter.values()):
                counter[s[j]] -= 1
                j += 1
            
            if all(cnt <= n//4 for cnt in counter.values()):
                min_size = min(min_size, j - i)
                
            counter[s[i]] += 1
            
        return min_size