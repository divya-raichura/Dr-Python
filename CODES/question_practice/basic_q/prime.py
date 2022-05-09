# print a list of prime numbers till a number inputed by user
import math

n = int(input("number till which prime number list should be printed: "))

count = 0


def isprime(x):
    global count
    sqr = int(math.sqrt(x))
    for i in range(2, sqr + 1):
        if x % i == 0:
            return False
    count += 1
    return True


prime = [i for i in range(2, n + 1) if isprime(i)]
print(prime)
print('no of prime numbers: ', count)

# method 2(from break.py):-
print("Method 2")
prime = []
for i in range(2, n + 1):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        prime.append(i)

print(prime)
