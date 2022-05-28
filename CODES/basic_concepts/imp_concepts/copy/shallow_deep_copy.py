# following will create a new variable cpy with same ref
# both point to same number 5
# org = 5
# cpy = org
# integers are immutable, so if we change cpy, it will not affect org
# cpy = 3
# print(org)  # 5
# print(cpy)  # 3

# in case of mutable object, it will change original
# eg, if its list, then it will change the element of list, similar to Java

# to do the copy in case of list like integers, we import copy module

import copy

org = [1, 2, 3, 4, 5]
# following are the ways to make copy:

# cpy = copy.copy(org)
# cpy = org.count()
# cpy = list(org)
# cpy = org[:]

# print('before', org)
# print('before', cpy)
# cpy[0] = 99
# print('after', org)
# print('after', cpy)

# shallow copy - one level deep, only references of nested child obj
# deep copy    - full independent copy

# wkt tuple is immutable, we cannot change inside element
# what if we have mutable obj like list inside tuple?
# tup = ([2, 3, 4, 5], [45, 34, 42, 87, 21])
# tup[1][3] = 'g'
# print(tup)
# yes! if inside we have a mutable object, we can change
# elements of that mutable object
# we can't change the mutable object itself, cause it's
# element of tuple, but inside that obj, we can change that obj's
# elements
# same with when we make list copy...

# to make copy inside too, we need to make deep copy
# cpy = copy.deepcopy(org)

