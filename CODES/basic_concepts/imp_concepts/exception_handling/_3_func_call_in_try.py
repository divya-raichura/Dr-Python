def divide(z):
    return 45 / z


try:
    print(divide(9))
    print(divide(92))
    print(divide(0))
    print(divide(34))
    print(divide(5))
except ZeroDivisionError:
    print('Error: Invalid argument.')

# The reason print(divide(34)) and print(divide(5)) is never
# executed is because once the execution jumps to the code in
# the except clause, it does not return to the try clause.
# Instead, it just continues moving down the program as normal.
