def mutable_eg(l):
    l.append(69)  # lis.append(69) did the same work
    print('inside:', l)


lis = [25, 6, 7, 8, 98]
print('before calling:', lis)
mutable_eg(lis)
print('after calling:', lis)

