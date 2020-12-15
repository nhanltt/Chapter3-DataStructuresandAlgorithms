# Program for checking if a string is parlindrome
# Writen by Nhan Thi Thanh Le
# at 12/09/2020
class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    
    print('Please enter the string you want to check !')
    print('Enter "exit" if you want to quit program !')
    while True:
        s = input("What's string you want to check? ")
        if s.lower() == 'exit':
            break
        checker = Deque()
        for i in s:
            checker.add_front(i)
        c = True
        while checker.size() > 1:
            if checker.remove_front() != checker.remove_rear():
                c = False
                break
        if not c:
            print(s," is not a parlindrome")
        else:
            print(s," is a parlindrome")
        