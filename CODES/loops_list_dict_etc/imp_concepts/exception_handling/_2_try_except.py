def divide(z):
    try:
        return 45 / z
    except ZeroDivisionError:
        print('Error: Invalid argument.')


print(divide(9))
print(divide(92))
print(divide(0))
print(divide(34))
print(divide(5))
# When code in a try clause causes an error, the program execution
# immediately moves to the code in the except clause. After running
# that code, the execution continues as normal.
