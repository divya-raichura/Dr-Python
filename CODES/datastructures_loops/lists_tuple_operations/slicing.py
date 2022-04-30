# https://www.pythontutorial.net/advanced-python/python-slicing/

a = [34, 56, 89, 25]
print(a[2:4])  # a:b means a is inclusive and b is exclusive
#  hence, tho 4 is out of bound, it doesn't give error because it is
#  exclusive and ends at 3

print(a[-2:])  # characters from the sec-last (included) to the end
# same as
print(a[-2:4])  # characters from the sec-last (included) to the end


# jump
print(a[::1])  # same as print(a[::]) ... prints array as it is

print(a[1:4:2])

# interesting
print(a[-1:])  # shows last element
print(a[:-1])  # shows elements from 0th index to sec-last
# reverse
print(a[-1::-1])
print(a[::-1])
print(a[-1:-4:-1])  # means -1 se chalu karu, -4 (exclusive) so -3 tak jao aur -1 jump karo hence piche jara
# if we don't jump -1 it goes ahead and ends, doesn't even print anything
print(a[-1:-4])
print(a[-4:-1])  # this prints 34 to 89

# hence, this means that we need to put lower indices first
# and then the indices at the end basically start:end:jump
# start<end otherwise it prints empty array
# hence, -4 ka index is smaller than -1 hence 2nd statement prints array and first one prints empty array
# print(a[-1::-1]) hence this in this reverse type...
# -1 to end which is last element and jump -1 ie after printing
# req element go for_while previous(as jump: -1) element
