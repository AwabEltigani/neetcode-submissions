class DoubleyLinkedList:
    def __init__(self,key,value,prev = None,next_ = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next_ = next_
    def set_value(self,new_value):
        self.value = new_value
    


class LRUCache:

    def __init__(self, capacity: int):
        self.current_size = 0
        self.max_size = capacity
        self.head = None
        self.tail = None
        self.hash_map = {}
    
    def recent_to_the_front(self,node):
        if self.head == node:
            return
        elif self.tail == node:
            tail = self.tail
            self.tail = self.tail.prev
            tail.prev = None
            self.tail.next_ = None
            tail.next_ = self.head
            self.head.prev = tail
            self.head = tail
        else:
            cur = node
            node.prev.next_ = node.next_
            node.next_.prev = node.prev
            cur.next_ = self.head
            self.head.prev = cur
            self.head = cur


    def get(self, key: int) -> int:
        if self.current_size == 0:
            return -1
        
        node = self.hash_map.get(key,None)
        if node is None:
            return -1
        
        self.recent_to_the_front(node)

        return node.value 
        
        

    def put(self, key: int, value: int) -> None:
        if self.current_size == 0:
            new_node = DoubleyLinkedList(key,value)
            self.hash_map[key] = new_node
            self.current_size += 1
            self.head = new_node
            self.tail = new_node
        else:
            cur_node = self.hash_map.get(key,None)
            if cur_node:
                cur_node.set_value(value)
                self.recent_to_the_front(cur_node)
            else:
                new_node = DoubleyLinkedList(key,value)
                self.hash_map[key] = new_node
                self.head.prev = new_node
                new_node.next_ = self.head
                self.head = new_node
                self.current_size += 1
                if self.current_size > self.max_size:
                    cur_tail = self.tail
                    self.tail = self.tail.prev
                    self.tail.next_ = None
                    cur_tail.prev = None
                    self.current_size -= 1
                    self.hash_map.pop(cur_tail.key)
                if self.head == self.tail:
                    self.tail = new_node
                self.recent_to_the_front(new_node)
                
                


        
