class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_freq = defaultdict(int)               
        self.freq_to_orddict = defaultdict(OrderedDict)   
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
        
        freq = self.key_to_freq[key]
        val = self.freq_to_orddict[freq][key]
        self.update(key, val)
        
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        
        if key in self.key_to_freq:
            self.update(key, value)
        
        else:
            if len(self.key_to_freq) == self.capacity:     
                min_key, min_val = self.freq_to_orddict[self.min_freq].popitem(last = False)  
                del self.key_to_freq[min_key]    
            
            self.min_freq = 1                            
            self.key_to_freq[key] = 1
            self.freq_to_orddict[1][key] = value
            
    def update(self, key, value):
date min_freq if neccessarry

        freq = self.key_to_freq[key]
        
        if self.min_freq == freq and len(self.freq_to_orddict[freq]) == 1:  
            self.min_freq += 1
            
        self.freq_to_orddict[freq].pop(key)    
        freq += 1                               
        self.key_to_freq[key] = freq            
        self.freq_to_orddict[freq][key] = value
