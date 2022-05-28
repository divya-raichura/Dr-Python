# here input will be taken as one element until you press enter
# once you press enter, it will consider another input
# till the range exceeds this will continue
# a = int(input("enter no of elements: "))
# b = []
# for i in range(a):
#     b.append(input())
# print(b)  # VIMP NOTE: it takes all input elements as string
# we can convert those elements in int using map()
# l = list(map(int, b))


# in below method every letter you press is a new element
# hence you can't add elements having more than one letter
# once you press enter, program ends and print executes
# n = list((input("enter elements: ")))
# print(n)

# best but... if you give input like 1  56 78 90
# then it takes it as string and thus gives invalid literal error
# l = [int(input()) for i in range(5)]
# print(l)

# VVV IMP
# so the best way to take input when it is to be given in one line
# is as follows:
# l = list(map(int, input().split()))
# print(l)


# https://stackoverflow.com/questions/11479392/what-does-a-for-loop-within-a-list-do-in-python
# note
# myList = []
# for i in range(10):
#     myList.append(i)

# is same as
# myList = [i for i in range(10)]
