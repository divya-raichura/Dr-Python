# how to remove elements from list while looping over it
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def even(x):
    return x & 1 == 0  # x % 2 == 0


# following method is wrong as when we remove element from list
# other element shift to left, and we miss the next number
# in the for loop
# for item in a:
# if even(item):
#     a.remove(item)


# correct methods:-

# method 1
# we loop over a copy of the list and then remove elements from the list
# for item in a[:]:
#     if even(item):
#         a.remove(item)

# method 2
# a = [x for x in a if not even(x)]

# method 3 more efficient that method 2
# a[:] = [x for x in a if not even(x)]

# method 4: use filter method
# z = list(filter(even, a))
# print(z)
