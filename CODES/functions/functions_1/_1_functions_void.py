# functional programming :-
# programming in which functions  are treated as first class citizens
# if we can treat functions in same way as variables
# then functions are first class citizens
# we can assign variables, swap, pass in arguments
# so if we do this with functions_1 then they are first class citizens
# which means programming language is functional programming language

def fun():
    print('divya raichura is the next elon musk')

# 1
# fun  # nothing happens # in jupyter random value is printed

# 2
# print(fun)  # prints some random value

# 3
# fun()  # calls the function and prints the value inside it

# 4
# print(fun())  # function is called implies statement is printed but also...
# 'none' is printed
# so if we print function_call() then the return value is printed
# so, to call a void function, do fun_call() instead of print(fun_call())



# 1
# a = fun()  # -> same as fun()
# calls the function and statement is printed inside console

# 2
# a()  # not callable

# 3
# print(a)  # -> same as print(fun()) except, this prints only none
# but statement is also printed as to do this we did a = fun()

# 4
# print(a())  # not callable error

# 1
# a = fun  # -> same as fun
# nothing happens in console but, a ab khud ek function hogya
# so jo kuch upar fun ke sath kiya same cheeze a karskta ab

# 2
# a # here nothing # in jupyter random
# same as fun

# 3
# print(a)  # -> same as print(fun)
# prints random value

# 4
# a()  # -> same as fun() above
# calls the function and that inside statement is printed

# 5
# print(a())  # -> same as print(fun())
# function is called and statement is printed but...
# 'none' is also printed as function returns 'none'

# cause in python wkt everything is an object
# so functions are also objects
# so fun is ref var in stack which points to actual function in heap
# we did a = fun so 'a' points to the same function now
# so 'a' and 'fun' now calls the same function as they point to same function
