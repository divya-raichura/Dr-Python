# data type :
# 1. immutable(cannot change value)
# 2. mutable (can change value)


#  1: numbers

a = 2  # int
b = 1.35  # float
c = 1 + 3j  # complex
print("type:", type(c), "\ninstance:", isinstance(c, complex))

#  2: string

#  3: lists_tuple_operations
list1 = [1, 2, 'divya']  # can change element and perform various
# ops like slicing [ : : ],  repeating strings * , concatenation +

#  4: tuple
# same like lists_tuple_operations but we cannot update the value inside it, ie its
# elements are immutable
tup = (1, 3, 45, 'divya')

#  dictionaries
d = {1: 'Jimmy', 2: 'Alex', 3: 'john', 4: 'mike'}
print(d, type(d), sep='\n')
print(d.keys())
print(d.values())

# set = returns changed seq of unique elements, can be created with two methods
# 1- built in method set()
# 2- passing elements inside curly bracket
set1 = set()
set1.add("elon")
print("set1:", set1)
set2 = {1, 3, 'divya', 3, 'divyar'}
set2.add(99)
print("set2:", set2)
