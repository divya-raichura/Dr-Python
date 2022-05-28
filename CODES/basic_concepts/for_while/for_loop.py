# https://www.javatpoint.com/python-for-loop

s = "Elon Musk"
# for in s:
#     print(ch, end='')
# print('\n')
# using index in for loops in python

for i in range(len(s)):
    print(i, s[i])

# instead of this we have a method called enumerate
# using this we can iterate over the iterators and also get
# their index value
for index, ch in enumerate(s):  # instead of just 'in s' we use 'in enumerate(s)'
    print(index, ch)  # same as :  print(index, s[index])

# # index, ch ... this thing happening above is known as tuppling
# a = 10
# b = 20
# swap a and b
# a, b = b, a
# internally what happens is
# first a tuple is created of rhs
# (b,a)=(20,10)
# then it is assigned to lhs ie
# (a,b)=(20,10) ... a <-- 20 and b <-- 10

# same thing is happening in enumerate
# it first creates rhs (index, value)
# then it is stored in lhs (index, ch)... index <-- index and ch <--value
# so enumerate returns rhs
