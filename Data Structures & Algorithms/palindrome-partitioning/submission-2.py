class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        data = []
        def isPalindrome(s,i,j):
            while j >= i:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True
        
        def bfs(index):
         
            if index > len(s) - 1:
                print(data.copy())
                res.append(data.copy())
                return

            
            for j in range(index,len(s)):
                if isPalindrome(s,index,j):
                    data.append(s[index:j+1])
                    bfs(j+1)
                    data.pop()
                    

        
        
        
        bfs(0)
        return res

