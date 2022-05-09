# import time
# import sys

size = int(input("how many element you want to enter?: "))
user = list(input("enter the element: ") for i in range(size))
print('your list: ', user)


# time.sleep(0.5)
# print("Now, printing the elements of this list as a nice string")
# print("Loading", end='')
# for_while i in range(3):
#     print(".", end='')
#     time.sleep(0.5)
# print()

def string(lst):
    s = ''
    if len(lst) == 0:
        return s
    if len(lst) == 1:
        return lst[0]
    for index, value in enumerate(lst):
        if index == (len(lst) - 2):
            s += value + ' and ' + lst[index + 1]
            return s
        s += value + ', '


print('in nice string way:', string(user))
