class MinStack:

    def __init__(self):
        self.q = []
        self.minv=None

    def push(self, val: int) -> None:
        if not self.q:
            self.minv = val
        else:
            if val <= self.minv:
                self.q.append(self.minv)
                self.minv = val
        self.q.append(val)

    def pop(self) -> None:
        if not self.q:
            return None
        else:
            y = self.q.pop()
            if y == self.minv and self.q:
                self.minv = self.q.pop()
            return y

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.minv