# Program for customer service system 
# Writen by Nhan Thi Thanh Le
# at 12/09/2020
import os
import time
class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def show(self):
        return self.items    


if __name__ == "__main__":
    
    c1 = 'NO'
    c2 = 'NO'
    ask = ''
    customer = Queue() 
    while ask != '4':

        print('Number of waiting customer',customer.size()) 
        if customer.size() != 0:
            print("Name of customers: ",customer.show())
        else :
            print("No one is waiting")
        print(f'At the counter 1: {c1}')
        print(f'At the counter 2: {c2}')
        print('1. Counter 1st get customer, 2. Counter 2nd get customer, 3. Customer is waiting, 4. Exit program')

        ask = input('Command: ')

        if ask == '3':
            name = input("What's your name? ")
            customer.enqueue(name)

        if (ask == '1') :
            if not customer.is_empty():
                c1 = customer.dequeue()
                print(f"Customer '{c1}' comes to counter 1 !!?")
                # print("remaining customer: ", customer.show())
            else:
                print('No customer is waiting')

        if (ask == '2') :
            if not customer.is_empty():
                c2 = customer.dequeue()
                print(f"Customer '{c2}' comes to counter 2 !!?")
                # print("remaining customer: ", customer.show())  
            else: 
                print('No customer is waiting')
        time.sleep(3)
        os.system('cls')
        






            



    
    