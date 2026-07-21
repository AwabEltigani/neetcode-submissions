class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store.keys():
            self.store[key] = [[value,timestamp]]
        else:
            print(self.store.get(key))
            print(timestamp,value)
            self.store.get(key).append([value,timestamp])
            print(self.store.get(key))
        

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        arr = self.store.get(key)
  
        l = 0
        r = len(arr) - 1

        if arr[0][1] > timestamp:
            return ""

        

        while r >= l:
            m = (r+l)//2
            if arr[m][1] == timestamp:
                return arr[m][0]
            elif arr[m][1] > timestamp:
                r = m - 1
                return arr[r][0]
            else:
                l = m + 1
                
        
        return arr[r][0]
        

        

        
