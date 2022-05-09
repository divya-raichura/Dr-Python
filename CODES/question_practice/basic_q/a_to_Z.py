# method 1
starting = 97
for i in range(starting, starting + 26):
    print(chr(i), end=' ')

print()
# method 2
for i in range(ord('a'), ord('z') + 1):
    print(chr(i), end=' ')

print()
# method 3
for i in range(0, 26):
    print(chr(ord('a') + i), end=" ")
    # character value of (aci value of a + 0 to 25)  # explained in java file

print()
# method 4
ans = ' '.join([chr(i) for i in range(97, 97 + 26)])  # by making
# changes in range() of for loop, we can make more methods
# but its same like above 3 method ke for loops like below, below
# one is better as above one seems like it is by-hearted
# test_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]
print(ans)

# count = 0
# for i in range(starting, starting + 26):
#     count += 1
#     print(i, end=' ')
#
# print()
# print(count)
