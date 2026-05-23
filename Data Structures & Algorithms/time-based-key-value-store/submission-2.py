class TimeMap:

    def __init__(self):

       self.timeKeyDict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeKeyDict.keys():
            self.timeKeyDict[key] = [[value,timestamp]]
        else:
            curArr = self.timeKeyDict.get(key)
            curArr.append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeKeyDict.keys():
            return ""

        
        
        curArr = self.timeKeyDict.get(key)
        target = timestamp

        if len(curArr) == 1:
            if curArr[0][1] <= target:
                return curArr[0][0]

        curArr.sort(key=lambda x: x[1])

       

        l = 0
        r = len(curArr) - 1
        maxLessThanOrEqualTo = 0

        while r >= l:
            mid = (r+l)//2
            if curArr[mid][1] == target:
                return curArr[mid][0]
            elif target >= curArr[mid][1]:
                maxLessThanOrEqualTo = max(curArr[mid][1],maxLessThanOrEqualTo)
                l = mid + 1
            else:
                r = mid - 1
            

        for i in range(len(curArr)):
            if maxLessThanOrEqualTo == curArr[i][1]:
                return curArr[i][0]
        
        return ""

        

        
