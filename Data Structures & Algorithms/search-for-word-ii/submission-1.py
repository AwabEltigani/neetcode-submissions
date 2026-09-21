class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        root = Trie()
        res = []
        ROWS,COLS = len(board),len(board[0])
        seen = set()
        if ROWS == 1 and COLS == 1:
            for word in words:
                if word == board[0][0]:
                    res.append(word)
                    return res

        for word in words:
            cur = root.root
            for i,char in enumerate(word):
                if char not in cur.children:
                    new_node = Node()
                    cur.children[char] = new_node
                    cur = new_node
                else:
                    cur = cur.children.get(char)
                if i == len(word) - 1:
                    cur.isEnd = True
        
        def dfs(root,i,j,cur_string):
            if root.isEnd == True:
                res.append(cur_string)
                root.isEnd = False
            if len(root.children) == 0 or board[i][j] not in root.children or (i,j) in seen:
                return

            cur_string += board[i][j]
            seen.add((i,j))
            if i > 0:
                dfs(root.children.get(board[i][j]),i - 1,j,cur_string)
            if i < ROWS - 1:
                dfs(root.children.get(board[i][j]),i + 1,j,cur_string)
            if j < COLS - 1:
                dfs(root.children.get(board[i][j]),i,j + 1,cur_string)
            if j > 0:
                dfs(root.children.get(board[i][j]),i,j - 1,cur_string)
            cur_string = cur_string[0:-1]
            seen.remove((i,j))
        for i in range(ROWS):
            for j in range(COLS):
                dfs(root.root,i,j,"")
        return res
                    
                





        