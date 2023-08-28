class MyStack:
    def __init__(self):
        self.main = deque()
        self.helper = deque()
    def push(self, x: int) -> None:
        self.main.append(x)
    def pop(self) -> int:
        while len(self.main) > 1:
            curr = self.main.popleft()
            self.helper.append(curr)
        curr = self.main.popleft()
        while self.helper:
            curr2 = self.helper.popleft()
            self.main.append(curr2)
        return curr
    def top(self) -> int:
        curr = 0
        while self.main:
            curr = self.main.popleft()
            self.helper.append(curr)
        while self.helper:
            curr2 = self.helper.popleft()
            self.main.append(curr2)
        return curr
    def empty(self) -> bool:
        return True if len(self.main) == 0 else False
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()