# this shows integers are immutable objects
# if you change value for one ref var, it doesn't change for other
# similarly if you assign new value to 'a' it won't update it
# ie it won't change og value, it will create new one and
# a will point to new value and og value will hit garbage collection
# again! you are not modifying og value
# you create new value which a points to
# same in JAVA
# a = 5
# print(a)
# b = a  # both ref var point to same obj
# print(b)
# b += 3
# print(a)
# print(b)
# a += 18
# print(a)

