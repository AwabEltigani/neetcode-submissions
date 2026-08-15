class DoubleyLinkedLists:
    def __init__(self,key=0,val = 0,prev = None,next_ = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next_ = next_

    def updateKey(self,new_val):
        self.val = new_val

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        new_node = self.hashmap.get(key)

        if new_node == self.head:
            pass
        elif new_node == self.tail:
            cur_tail = self.tail
            new_tail = self.tail.prev
            new_tail.next_ = None
            cur_tail.prev = None
            self.tail = new_tail
            cur_tail.next_ = self.head
            self.head.prev = cur_tail
            self.head = cur_tail
        else:
            new_node.prev.next_ = new_node.next_
            print(new_node.val)
            new_node.next_.prev = new_node.prev
            new_node.next_ = self.head
            self.head.prev = new_node
            self.head = new_node
    
        
        
        return self.hashmap.get(key).val
        
    def put(self, key: int, value: int) -> None:
        if self.size == 0:
            new_node = DoubleyLinkedLists(key,value)
            self.head = new_node
            self.tail = new_node
            self.hashmap[key] = new_node
            self.size += 1
        else:
            new_node = self.hashmap.get(key,None)
            if new_node is not None:
                new_node.updateKey(value)
            else:
                new_node = DoubleyLinkedLists(key,value)
                new_node.next_ = self.head
                self.head.prev = new_node
                self.head = new_node
                self.size += 1
                self.hashmap[key] = new_node
                if self.size > self.capacity:
                    cur_tail = self.tail
                    new_tail = self.tail.prev
                    self.tail.prev = None
                    new_tail.next_ = None
                    self.tail = new_tail
                    self.size -= 1
                    self.hashmap.pop(cur_tail.key)
            if new_node == self.head:
                pass
            elif new_node == self.tail:
                cur_tail = self.tail
                new_tail = self.tail.prev
                new_tail.next_ = None
                cur_tail.prev = None
                self.tail = new_tail
                cur_tail.next_ = self.head
                self.head.prev = cur_tail
                self.head = cur_tail
            else:
                new_node.prev.next_ = new_node.next_
                new_node.next_.prev = new_node.prev
                new_node.next_ = self.head
                self.head.prev = new_node
                self.head = new_node


                


            

            

        
