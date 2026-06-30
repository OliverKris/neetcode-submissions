class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum == []:
            self.minimum.append(val)
        else:
            min = self.minimum.pop()
            self.minimum.append(min)
            if val <= min:
                self.minimum.append(val)
            else:
                self.minimum.append(min)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        top = self.stack.pop()
        self.stack.append(top)
        return top

    def getMin(self) -> int:
        min = self.minimum.pop()
        self.minimum.append(min)
        return min
