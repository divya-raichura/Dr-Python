user = int(input('''till which number you want to print fibonacci number: '''))


def fib(inp):
    """print fibonacci series till nth fibo number (n-user input)"""
    a, b = 0, 1
    count = 0
    while count <= inp:
        print(a, end=' ')
        a, b = b, a + b
        count += 1


def fib_2(inp):
    """Prints fibonacci series till asked number"""
    a, b = 0, 1
    while a < inp:  # note: here we do not have count var
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(user)
