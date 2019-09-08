import math
from decimal import Decimal

def mu (a, b):
    # takes two numbers and outputs the difference in percents
    x = float (a)
    y = float (b)
    c = x - y
    d = c/y
    print ("{:.2%}".format(d))

print ("Коммерсант:")
mu (18652885,22130731)
print ("Ведомости:")
mu (12044459, 8932893)
print ("РБК:")
mu (67519403, 68834953)
print ("Дождь:")
mu (2384525,2440516)
print ("Republic:")
mu (452928, 477538)


def takeme ():
    print ()