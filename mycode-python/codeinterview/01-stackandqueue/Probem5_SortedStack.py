class SortedStack:
    def __init__(self):
        self.stack = list()
        self.help = list()

    def push(self, value):
        self.stack.append(value)

    def sort_stack(self):
        if len(self.stack) == 0:
            return self.stack
        while len(self.stack) > 0:
            cur = self.stack.pop()
            while len(self.help) > 0 and cur > self.help[-1]:
                help_top = self.help.pop()
                self.stack.append(help_top)
            self.help.append(cur)

        while len(self.help) > 0:
            self.stack.append(self.help.pop())

if __name__ == '__main__':
    sortStack = SortedStack()
    sortStack.push(3)
    sortStack.push(1)
    sortStack.push(6)
    sortStack.push(2)
    sortStack.push(5)
    sortStack.push(4)

    sortStack.sort_stack()
    print sortStack.stack