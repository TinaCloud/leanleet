class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.m.keys():
            self.m[key] = 1
        else:
            self.m[key] += 1
    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.m.keys():
            return 
        else:
            if self.m[key] == 1:
                del self.m[key]
            elif self.m[key] > 1:
                self.m[key] -= 1

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if not self.m:
            return ""
        else:
            return max(self.m, key=self.m.get)

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if not self.m:
            return ""
        else:
            return min(self.m, key=self.m.get)


    