def __init__(self):
    """
    initialize your data structure here.
    """
    self.stack = []


def push(self, x: int) -> None:
    if self.stack:
        self.stack.append((x, min(x, self.stack[-1][1])))
    else:
        self.stack.append((x, x))


def pop(self) -> None:
    if self.stack:
        return self.stack.pop()


def top(self) -> int:
    if self.stack:
        return self.stack[-1][0]
    else:
        return None


def getMin(self) -> int:
    return self.stack[-1][1]