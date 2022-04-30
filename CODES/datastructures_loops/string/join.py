# join() method is called on a string, gets passed a list of
# strings, and returns a string. The returned string is the
# concatenation of each string in the passed-in list.

# NOTE: the string that join() calls on is inserted between
# each string of the list argument.

# Remember that join() is called on a string value and is
# passed a list value. (It’s easy to accidentally call it the
# other way around.)
lst = ['mummy', 'papa', 'vedika', 'divya']
print(' and '.join(lst))  # ' and ' is inserted in place of each comma in lst


