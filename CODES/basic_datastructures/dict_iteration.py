
# note: We can use numbers, strings, or tuples as the key, but we
# cannot use any mutable object like the list as the key in the
# dictionary.

dictionary = {'name': 'elon', 'age': 50, 'job': 'entrepreneur', 'feat': 'billionaire'}

# prints keys
# for i in dictionary:
#     print(i)

# prints values
# for i in dictionary:
#     print(dictionary[i])

# using values() method.
# for i in dictionary.values():
#     print(i)

#  to print the items of the dictionary by using items() method.
# method 1
for i in dictionary.items():
    print(i)
# method 2
for i, j in dictionary.items():
    print(i, j)
