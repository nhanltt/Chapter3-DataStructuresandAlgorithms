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
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def dec_to_base(n, base):
    digits = '0123456789ABCDE'
    bin_num = Stack()
    while n != 0:
        bin_num.push(n%base)
        n //= base
    num_bin = ""
    while not bin_num.is_empty():
        num_bin += str(digits[bin_num.pop()])
    return num_bin

if __name__ == "__main__":
    n, base = input().split(' ')
    print(dec_to_base(int(n), int(base)))