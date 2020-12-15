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


def check_type(a, b):
    if (a == ')' and b == '(') or (a == ']' and b == '[') or (a == '}' and b == '{'):
        return True
    return False


def par_check(s):
    stock = Stack()
    check = True
    i = 0
    l = len(s)
    while check and i != l:
        if (s[i] == '(') or (s[i] == '[') or (s[i] == '{'):
            stock.push(s[i])
        else:
            if stock.is_empty():
                return False
            else:
                if check_type(s[i], stock.peek()):
                    stock.pop()
                else:
                    return False
        i += 1
    if (not check) or (not stock.is_empty()):
        return False
    return True


print(par_check("{{()[][][[]]}}"))
