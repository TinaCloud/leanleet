class NumMatrix:
    def __init__(self, matrix):
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        if n == 0:
            return
        self.nums = [[0 for j in range(n)] for i in range(m)]
        self.BIT = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])

    def _lowbit(self, a):
        return a & -a

    def update(self, row, col, val):
        m, n = len(self.nums), len(self.nums[0])
        diff = val - self.nums[row][col]
        self.nums[row][col] = val
        i = row + 1
        while i <= m:
            j = col + 1
            while j <= n:
                self.BIT[i][j] += diff
                j += (self._lowbit(j))
            i += (self._lowbit(i))

    def getSum(self, row, col):
        res = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                res += self.BIT[i][j]
                j -= (self._lowbit(j))
            i -= (self._lowbit(i))
        return res

    def sumRegion(self, row1, col1, row2, col2):
        return self.getSum(row2, col2) - self.getSum(row2, col1 - 1) \
               - self.getSum(row1 - 1, col2) + self.getSum(row1 - 1, col1 - 1)
