class MinStack:
    
    def __init__(self):
        self.minStack = []
        self.currentMin = 0
        

    def push(self, val: int) -> None:
        if len(self.minStack) == 0:
            self.currentMin = val
        else:
            self.currentMin = min(self.currentMin,val)
        self.minStack.append([val,self.currentMin])


    def pop(self) -> None:
        self.minStack.pop()
        if len(self.minStack) <= 0:
            return
        
        currentTop = self.minStack[len(self.minStack) - 1]
        self.currentMin = currentTop[1]

    def top(self) -> int:
        currentTop = self.minStack[len(self.minStack) - 1]
        return currentTop[0]

    def getMin(self) -> int:
        currentTop = self.minStack[len(self.minStack) - 1]
        return currentTop[1]
        
