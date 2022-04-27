user = int(input('''till which number you want to print fibonacci number: '''))


def fib(inp):
    """print fibonacci series till nth fibo number (n-user input)"""
    a, b = 0, 1
    count = 0
    while count <= inp:
        print(a)
        a, b = b, a + b
        count += 1


fib(user)
