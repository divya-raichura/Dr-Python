# Right now, getting an error, or exception, in your Python
# program means the entire program will crash
def divide(z):
    return 45 / z  # from the line number in error we know that
    # this return statement is causing error


print(divide(9))
print(divide(92))
print(divide(0))
print(divide(34))
print(divide(5))

# the program crashes when it divides by zero
# we want programs to detect errors, handle them, and then
# continue to run. For this purpose we use try_except
