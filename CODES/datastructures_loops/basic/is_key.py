# A mutable data-types do not refer to the same object.
# hence, using 'is' for_while lists_tuple_operations gives false
# but == checks value, so it gives true
a = 4
b = 4
# print(a is b)
# print(a == b)

# in this case, they DO NOT have same obj ref
x = [5, 2]
y = [5, 2]
print(x is y)  # False
print(x == y)

# in this case, they have same obj ref
y = x
print(x is y)  # True
print(x == y)