# lis = [
#     [3, 4, 5],
#     [67, 22, 11],
#     [2]
# ]
# print(lis[1][2])
# print(lis)

# printing list using nested for_while loop
# for_while i in range(0, len(lis)):  # this iterates through row
#     for_while j in range(0, len(lis[i])):  # this iterates through every element(col) in that row
#         print(lis[i][j], end=' ')  # prints that element
#     print()  # for_while printing new line after a all elements of a row are printed


# printing all tables from 1 to 10

# for_while i in range(1, 11):
#     inner = [i * j for_while j in range(1, 11)]
#     print(inner)
# but it created various list and printed it


# we want to create single list and add all these lists_tuple_operations in that single list
table = [[i * n for i in range(1, 11)] for n in range(1, 21)]
