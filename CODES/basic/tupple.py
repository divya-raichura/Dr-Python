# they are immutable
# but if the element inside tuple is mutable, we can change that element
t = (2, 45, 6)
a = (2, 45, 6)
print(t is a)  # True
# t[3] = 335 can't do this
tup = ([2, 3], [456, 7])
tup[1][0] = 33  # can be done
print(tup)
# tup[1] = [256,6] can't do this
