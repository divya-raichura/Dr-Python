# input user to print table as per input
user = int(input())
table_single_1d = [i * user for i in range(1, 11)]
# print(table_single_1d)

# for printing table from 1 to user
table_double_2d = [[i * n for i in range(1, 11)] for n in range(1, user + 1)]
print(table_double_2d)
