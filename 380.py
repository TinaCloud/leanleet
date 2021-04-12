class RandomizedSet:

    def __init__(self):
        self.top_key = 0
        self.value_dict = {}
        self.key_dict = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.value_dict:
            self.value_dict[val] = self.top_key
            self.key_dict[self.top_key] = val
            self.top_key += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.value_dict:
            used_key = self.value_dict[val]
            self.top_key -= 1
            if used_key != self.top_key:
                replaced_value = self.key_dict[self.top_key]
                self.key_dict[used_key] = replaced_value
                self.value_dict[replaced_value] = used_key
            del self.value_dict[val]
            del self.key_dict[self.top_key]
            return True
        return False

    def getRandom(self) -> int:
        return self.key_dict[random.randint(0,self.top_key-1)]
