def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


user = int(input("Enter number: "))
collatz_ans = collatz(user)
while collatz_ans != 1:
    collatz_ans = collatz(collatz_ans)
else:
    print("done")
