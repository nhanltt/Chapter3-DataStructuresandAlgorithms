# Program to calculate with postfix form
# Writen by Nhan Thi Thanh Le
# at 12/09/2020


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


# Calculate 2 elements
def cal(a,b,i):
    if i == '+':
        return a + b
    if i == '-':
        return a - b
    if i == '*':
        return a * b
    if i == '/':
        return a / b
    return('can not calculate')


if __name__ == "__main__":
    s = input()
    # Create new stack that keep number 
    num = Stack()
    check = True
    for i in s:
        if i in '0123456789':
            num.push(int(i))
        if i in '+-*/':
            if num.size() >= 2: 
                b = num.pop() 
                a = num.pop()
                num.push(cal(a,b,i)) #Add result to stack for next calculation
            else: 
                print("not enough variable")
                check = False
                break
    if num.size() == 1 and check: # check if has any error. if not, print the result
        print(num.peek())  
    else:
        print('Please check your input')      


