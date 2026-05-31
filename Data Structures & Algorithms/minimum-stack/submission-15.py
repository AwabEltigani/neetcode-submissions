class MinStack:

    

    def __init__(self):
        self.stack = []
        self.curMin = 0

    def top(self) -> int:
        return self.stack[-1][0]

    def push(self, val: int) -> None:
        if len(self.stack) != 0:
            curTop = self.stack[-1][1]
            if curTop > val:
                self.stack.append([val,val])
                self.curMin = val
            else:
                self.stack.append([val,self.curMin])
        else:
            self.stack.append([val,val])
            self.curMin = val
    def pop(self) -> None:
        lastItem = self.stack[-1]
        if len(self.stack) > 1 and self.curMin == lastItem[1]:
            self.curMin = self.stack[-2][1]
        self.stack = self.stack[:-1]
        

    def getMin(self) -> int:

        return self.stack[-1][1]
        
