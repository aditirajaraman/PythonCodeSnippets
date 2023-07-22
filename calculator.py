# # print ("enter a")
#
# val1 = input("Enter number: ")
# a = 12
# b = 19
# add = int(val1) + b
# sub = b - int(val1)
# multiply = a * int(val1)
#
# print(a)
# print(b)
# print(add)
# print(sub)
# print(multiply)

#version 2

import math

t = int(input("enter first number: "))
h = int(input("enter second number: "))
operator = input("what operation: ")

# a - Add
# s - Subtract
# m - multiply

if operator == "a":
    result = t + h
elif operator == "s":
    result = h - t
elif operator == "m":
    result = t * h
elif operator == "sq":
    result = math.sqrt(h)
else:
    result = -1
    print("wrong operator")

print("result: " + str((result)))
