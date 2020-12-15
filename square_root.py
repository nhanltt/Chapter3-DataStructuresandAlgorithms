from tabulate import tabulate
import math

epsilon = 0.0000001


def my_square_root(a):
    x = 10
    while True:
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            return y
        x = y

data = []
for i in range(1, 10):
    a = my_square_root(i)
    b = math.sqrt(i)
    data.append([i,a, b, abs(a - b)])
print(tabulate(data, headers = ["a", "mysqrt(a)", "math.sqrt(a)", "diff"]))

