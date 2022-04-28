# def fun():
#     # global spam # spam becomes global only for this function
#     spam = 'local fun'
#     print(spam)
#     nuf()
#     print(spam)
#
#
# def nuf():
#     spam = 'fun ka ulta'
#     print(spam)
#
#
# # global spam doesn't do anything
# spam = "global"
# print(spam)
# fun()
# print(spam)

# global is only for telling 'functions' to use global scope variable


# following gives error because
# If you try to use a local variable in a function before you
# assign a value to it, as in the following program, Python
# will give you an error.

# in my words: when you haven't made eggs in function, it
# uses the global eggs but when you make eggs but below the print
# python sees that as normal code where you are printing/using
# variable before declaring it, hence it will give error then
# if you declare it above, then it uses it as local scope
# and if you don't declare it uses global one!

def spam():
    print(eggs)  # ERROR!
    # eggs = 'spam local'


eggs = 'global'
spam()

# This error happens because Python sees that there is an
# assignment statement for eggs in the spam() function ➊
# and, therefore, considers eggs to be local. But because
# print(eggs) is executed before eggs is assigned anything,
# the local variable eggs doesn't exist. Python will not fall
# back to using the global eggs variable ➋.
