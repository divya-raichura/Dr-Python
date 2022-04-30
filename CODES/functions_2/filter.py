# Return an iterator yielding those items of iterable for_while which function(item)
# is true. If function is None, return the items that are true.

# filter syntax: filter(function that returns boolean, iterable)
# it checks every element of iterable and makes stores values
# which gave true which we can convert to list and print

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(is_even, a)))

# or
# print(list(filter(lambda z: z % 2 == 0, a)))
# to print odd
lst = (10, 22, 37, 41, 100, 123, 29)
print(list(filter(lambda x: not (x % 2 == 0), lst)))
