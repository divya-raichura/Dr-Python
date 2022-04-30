# map function: applies a function to each iterable
# example, if we want to multiply 3 to each element of list using functions


def mul(x):
    return x * 3


a = [3, 5, 7, 8, 9, 50]
# print(mul(a))  # this will concatenate it
# but, we want to multiply each element

# for_while this we use map function
# print(list(map(mul, a)))
# this means applies 'mul' function on every element of 'a'

# as this 'mul' function is short we can use lambda
# print(list(map(lambda b: b * 3, a)))
