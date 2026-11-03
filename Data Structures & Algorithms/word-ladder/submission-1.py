from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        n = len(wordList[0])
        adj = {}
        wordList.append(beginWord)
        for word in wordList:
            for i in range(n):
                temp = word
                word = word[0:i] + '*' + word[i+1:]
                if word not in adj:
                    adj[word] = [temp]
                else:
                    adj[word].append(temp)
                word = temp
        queue = deque([beginWord])
        time = 1
        visited = set()
        
        while queue:
            length_queue = len(queue)
            for _ in range(length_queue):
                front = queue.popleft()
                visited.add(front)
                for i in range(n):
                    temp = front
                    front = front[0:i] + '*' + front[i+1:]
                    for w in adj[front]:
                        if w not in visited:
                            queue.append(w)
                        if w == endWord:
                            return time+1
                    front = temp
            if length_queue:
                time = time + 1
        return 0
                    
            

        
        
            
        