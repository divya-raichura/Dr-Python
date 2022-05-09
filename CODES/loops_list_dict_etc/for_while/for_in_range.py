# we can use for_while with else loop : https://www.javatpoint.com/python-for-loop

# range(start,stop,step size)


# printing the table using for_while in range

# note: range(4) means... 0 --> 1 --> 2 --> 3
# n = int(input('enter a number whose table you want to print: '))
# for multiplier in range(1, 11):
#     print(f'{n} x {multiplier} =', n * multiplier)

# lis = ["Divya", "Kunal", "Elon"]
# for i in range(len(lis)):
#     print("hello", lis[i] + '!')

# loop doesn't run for this
# for var_name in range(0):
#     print('1')


# hence, we do row + 1 so that no of rows is as requested by input
# as if we just write range(row) eg if row = 4 ==> range(4)
# then range will be 0->1->2->3... outer loop will run 4 times
# but when outer loop = 0, inner loop will have in range(0), so the
# inner loop won't run
# summary: outer loop runs : 4 times as req by user
#          inner loop runs : 3 times which is wrong
# hence we do row + 1, so that if row = 4 => row + 1 = 5 => range(5)
# and range will be 0->1->2->3->4
# so that, outer loop runs : 5 times but,
#          inner loop runs : 4 times as req by user
# User input for_while number of rows
# rows = int(input("Enter the rows:"))
# Outer loop will print number of rows
# for i in range(rows):
# Inner loop will print number of Asterisk
# row no = no of asterisk
# for j in range(i):
#     print("*", end='')
# print()

# making list using range
# a = list(range(1, 10, 2))
# print(a)

# making list using for in range
# a = [i for i in range(1, 11)]
# print(a)

# making a list of a table like this using for_while inside it
# table = [n * i for i in range(1, 11)]
# print(table)

# similarly, we can print table from 1 to n in single list (2d list)
# in one line, see @2d_list or @table_using_for
# n = int(input("no till which you want to print tables"))
# print([[n * i for i in range(1, 11)] for n in range(1, n + 1)])
