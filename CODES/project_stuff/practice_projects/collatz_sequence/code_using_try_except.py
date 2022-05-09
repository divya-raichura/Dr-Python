def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


try:
    user = int(input("Enter number: "))
    collatz_ans = collatz(user)
    while collatz_ans != 1:
        collatz_ans = collatz(collatz_ans)
    else:
        print("done")
except ValueError:
    print("You must enter an integer value!")

# Misunderstood try_except!
# What mistake I was doing :-
# try except means when your code runs, and you get an error like
# zero division error then program stops and gives error,
# so we put try except there so that when this error comes
# it displays message and continues program, doesn't crash/stop

# in this program:
# input takes string value, so input is actually '2'(str) not 2 (int)
# so we convert string to integer using int()
# though we use int(), this int()
# is only for_while integers which are string 'integer' not a 'string/character'
# note that if we type 'w' then it throws 'value error'
# we want to fix this error by using try_except
# what i was doing is i was removing int() which gives 'type error'
# and except clause was still 'value error'
# so if we put 'type error' then it will run except for_while all
# as input() is taking string values always

# hence, in case of int(input())
# we use try_except so that if input is any letter or string
# then except will run and program doesn't crash
# in code.py when we enter some string value program crashes
# so, try_except here prevents it
# this is the use of try_except
