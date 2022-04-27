# print a list of prime numbers till a number inputed by user
import math

n = int(input("number till which prime number list should be printed: "))

count = 0


def isprime(x):
    global count
    sx = int(math.sqrt(x))
    for i in range(2, sx + 1):
        if x % i == 0:
            return False
    count += 1
    return True


prime = [i for i in range(2, n + 1) if isprime(i)]
print(prime)
print('no of prime numbers: ', count)




