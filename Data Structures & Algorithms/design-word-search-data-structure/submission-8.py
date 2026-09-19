def dfs(root,cur_word):
        if len(cur_word) == 0:
            return root.isEnd
        
        if len(root.children) == 0:
            return False

        if cur_word[0] != "." and cur_word[0] not in root.children:
            return False
        if cur_word[0] == ".":
            for key in root.children:
                isFound = dfs(root.children.get(key),cur_word[1:])
                if isFound == True:
                    return True
                
        else:
            isFound = dfs(root.children.get(cur_word[0]),cur_word[1:])
            if isFound == True:
                return True
            
        return False
        
        


class Node:
    def __init__(self,isEnd):
        self.children = {}
        self.isEnd = isEnd
    


class WordDictionary:

    def __init__(self):
        self.root = Node(False)
    
    

    def addWord(self, word: str) -> None:
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
        for i,char in enumerate(word):
            if char == ".":
                isFound = dfs(cur,word[i:])
                return isFound
            if char in cur.children:
                cur = cur.children.get(char)
            else:
                return False
        return cur.isEnd
    

        
