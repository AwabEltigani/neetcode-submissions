class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[value,timestamp]]
        else:
            self.store.get(key).append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.store:
            return res
        
        arr = self.store.get(key)

        if len(arr) == 1:
            if timestamp < arr[0][1]:
                return ""
        
        l = 0
        r = len(arr)

        while r > l:
            m = (r+l)//2
            print(m)
            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = l + 1
            else:
                r = r - 1
                
        
        return res
            
        
        
