class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if self.stack1:
            self.stack1.append(x)
        else:
            self.stack2.append(x)

    def pop(self) -> int:
        if self.stack1:
            for _ in range(len(self.stack1)-1):
                self.stack2.append(self.stack1.pop())
            value = self.stack1.pop()
            for _ in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
            return value
        else:
            for _ in range(len(self.stack2)-1):
                self.stack1.append(self.stack2.pop())
            value = self.stack2.pop()
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            return value
        
    def peek(self) -> int:
        if self.stack1:
            return self.stack1[0]
        else:
            return self.stack2[0]

    def empty(self) -> bool:
        return not(self.stack1 or self.stack2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()