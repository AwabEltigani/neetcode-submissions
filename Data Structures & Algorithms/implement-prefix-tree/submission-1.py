class Node:
    def __init__(self,isEnd):
        self.children = {}
        self.isEnd = isEnd

class PrefixTree:
    count = 0
    def __init__(self):
        self.root = Node(False)

    def insert(self, word: str) -> None:
        cur = self.root
        for i,char in enumerate(word):
            if char not in cur.children:
                new_node = Node(False)
                cur.children[char] = new_node
                cur = new_node
            else:
                cur = cur.children.get(char)
            if i == len(word) - 1:
                cur.isEnd = True
        
    def search(self, word: str) -> bool:
        cur = self.root
       
          
        for char in word:
            if char not in cur.children:
                return False
            else:
                cur = cur.children.get(char)
        
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            else:
                cur = cur.children.get(char)
        
        return True
        