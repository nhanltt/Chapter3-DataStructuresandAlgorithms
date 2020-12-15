class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def par_check(s):
    stock = Stack()
    i = 0
    l = len(s)
    while i != l:
        if (s[i] == '('):
            stock.push(s[i])
        else:
            if stock.is_empty():
                return False
            else:
                if stock.peek() == '(':
                    stock.pop()
                else:
                    return False
        i += 1
    if (not stock.is_empty()):
        return False
    return True


print(par_check("())"))
