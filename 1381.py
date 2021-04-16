class CustomStack:

    def __init__(self, max_size: int):
        self.st = []
        self.max_size = max_size

    def push(self, x: int) -> None:
        if len(self.st) < self.max_size:
            self.st.append(x)

    def pop(self) -> int:
        if len(self.st) == 0:
            return -1
        return self.st.pop()

    def increment(self, k: int, val: int) -> None:    
        for i in range(k):
            if i >= len(self.st):
                break
            self.st[i] += val
