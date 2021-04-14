class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        x = True
        if val in self.l:
            x = False
        self.l.append(val)
        return x

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.l:
            return False
        else:
            self.l.remove(val)
            return True



    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        x = random.randint(0, len(self.l) - 1)
        return self.l[x]
