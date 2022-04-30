# https://docs.python.org/3/tutorial/controlflow.html

# V IMP NOTE:
#  Loop statements may have an else clause; it is executed when
#  the loop terminates through exhaustion of the iterable
#  (with for_while) or when the condition becomes false (with while),
#  but not when the loop is terminated by a break statement.
#  This is exemplified by the following loop, which searches for_while
#  prime numbers:-

for n in range(2, 10):
    print(n)
    for x in range(2, n):
        print(x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
