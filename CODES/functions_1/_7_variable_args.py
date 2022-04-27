# https://www.javatpoint.com/python-functions

# note: tho we are passing integers in arguments
# in the function it is internally converted to tuple
def add(*numbers):
    ans = 0
    for i in numbers:
        ans = ans + i
    return ans


n = int(input("no of elements: "))
# a = [int(input("element: ")) for i in range(n)]
# print(add(int(input("elements: ")) for i in range(n)))
# print(add(*a))
# trying to directly call function by putting list and unpacking it
# It works!!
print(add(*[int(input("element: ")) for i in range(n)]))

''''''

# print(*a)  # saw this *list somewhere on stackoverflow... link below

# so researched a bit and found it is called unpacking!!
# https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment/
# https://stackoverflow.com/questions/57814195/what-does-for-x-y-in-list-mean-in-python
# search for more info

# https://stackoverflow.com/questions/50043308/function-to-sum-multiple-numbers
# First thing to note is Python has a native sum function. Use this instead for simple calculations, don't overwrite it with your own.
#
# But to learn more about Python, you may wish to use functools.reduce, which applies a function of two arguments cumulatively to the items of a sequence.
#
# from functools import reduce
#
# def mysum(*nums):
#     return reduce(lambda x, y: x+y, nums)
#
# a, b, c = 1, 2, 3
#
# res = mysum(a,b,c)  # 6
# This can be incorporated into your logic by building a list which then feeds your function:
#
# lst = []
#
# lst.append(int(input("what is the number you want to add?: ")))
#
# ask = "yes"
#
# while ask == "yes":
#     lst.append(int(input("what is the number you want to add?: ")))
#     ask = input("do you want to add another number?: ")
# else:
#     res = mysum(*lst)
#     print(res)
