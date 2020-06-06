# stack

class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, data):
        self.items.append(data)
        self.top += 1

    def pop(self):
        if self.top > -1:
            del self.items[self.top]
            self.top -= 1
            return
        print('empty stack')

    def peep(self):
        if self.top >= 0:
            print(self.items[self.top])
            return
        print('empty')

    def show(self):
        print(self.items)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.show()
s.push(4)
s.pop()
s.pop()
s.show()
s.pop()
s.peep()
s.pop()
s.show()
s.pop()
