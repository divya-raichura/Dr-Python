n = int(input("pattern rows: "))  # 5

# to print
#    *
#    * *
#    * * *
#    * * * *
#    * * * * *

for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()


# to print
#     * * * * *
#     * * * *
#     * * *
#     * *
#     *

# for i in range(n):
#     for j in range(n - i):
#         print('*', end=' ')
#     print()


# to print
#           *
#         * *
#       * * *
#     * * * *
#   * * * * *

# for i in range(n):
#     spaces = n - 1 - i
#     for j in range(spaces):
#         print(' ', end=' ')
#     for k in range(i + 1):
#         print('*', end=' ')
#     print()


# to print
#            *
#          * * *
#        * * * * *
#      * * * * * * *
#    * * * * * * * * *

# for i in range(n):
#     spaces = n - 1 - i
#     for j in range(spaces):
#         print(' ', end=' ')
#     for k in range(i):  # remove i '+ 1' from here or from for_while loop below
#         print('*', end=' ')
#     for j in range(i + 1):
#         print('*', end=' ')
#     print()
