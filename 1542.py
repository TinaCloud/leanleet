class Solution:
    def longestAwesome(self, s: str) -> int:
        table = {0 : -1}
        count = [0] * 10
        res = 0
        for i in range(len(s)):
            count[int(s[i])] += 1
            key = self.convert(count)
            if key in table:
                res = max(res, i - table[key])

            for k in range(10):
                newKey = key
                if ((key>>k)&1)==0:
                    newKey += (1<<k)
                else:
                    newKey -= (1<<k)
                if newKey in table:
                    res = max(res, i - table[newKey])
            if key not in table:
                table[key] = i
        return res

    def convert(self, count):
        key = 0
        for i in range(10):
            key += ((count[i]%2)<<i)
        return key



    