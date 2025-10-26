class LRUCache:

    def __init__(self, capacity: int):
         #if capacity < 1:
            #error
        self.capacity = capacity
        self.list = OrderedDict()       

    def get(self, key: int) -> int:
        if key in self.list:
            self.list.move_to_end(key, last = False)
            return self.list[key]
        else: 
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.list:
            self.list[key] = value
            self.list.move_to_end(key, last = False)
        elif len(self.list) == self.capacity:
            self.list.popitem(last = True)
            self.list[key] = value
            self.list.move_to_end(key, last = False)
        else:
            self.list[key] = value
            self.list.move_to_end(key, last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)