# here input will be taken as one element until you press enter
# once you press enter, it will consider another input
# till the range exceeds this will continue
a = int(input("enter no of elements: "))
# b = []
# for_while i in range(a):
#     b.append(input())
# print(b)

# in below method every letter you press is a new element
# hence you can't add elements having more than one letter
# once you press enter, program ends and print executes
# n = list((input("enter elements: ")))
# print(n)

# best
l = [int(input()) for i in range(a)]
print(l)

# https://stackoverflow.com/questions/11479392/what-does-a-for-loop-within-a-list-do-in-python
# note
# myList = []
# for_while i in range(10):
#     myList.append(i)

# is same as
# myList = [i for_while i in range(10)]
