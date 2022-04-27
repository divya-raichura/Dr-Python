def hello(x):
    print(x, 'world')


# we can write small functions like above by using lambda
hello_ = lambda x: print(x, 'world')
hello('hello')
hello_('hi')


def add(a, b):
    return a + b


add_ = lambda a, b: a + b
print(add(51, 14))
print(add_(52, 26))
