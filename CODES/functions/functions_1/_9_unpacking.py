# https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment/
# https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
# https://geekflare.com/python-unpacking-operators/
a = (i ** 3 for i in range(5))
print(a)
print(list(a))
print(*a)

# can unpack generators as well
