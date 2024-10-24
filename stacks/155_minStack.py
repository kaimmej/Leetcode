class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        # print(f"Push {val=}")
        self.stack.append(val)
        if self.min == None or self.min > val:
            self.min = val

    def pop(self) -> None:
        
        topElement = self.top()
        # print(f"Pop {topElement=}")
        self.stack.pop()
        if self.min == topElement:
            # find new min... 
            self.findMin()

    def top(self) -> int:
        topElement = self.stack[-1]
        return topElement
    
    def findMin(self) -> None:
        # print("FIND MIN")
        if not self.stack:
            self.min = None
        else:
            smallest = self.stack[-1]
            for i in self.stack:
                smallest = min(i, smallest)
            self.min = smallest
        # print(self.min)
    def getMin(self) -> int:
        return self.min;
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()