n = int(input("pattern rows: "))  # 5

# to print
#    *
#    * *
#    * * *
#    * * * *
#    * * * * *

# for_while i in range(n):
#     for_while j in range(i + 1):
#         print('*', end=' ')
#     print()


# to print
#     * * * * *
#     * * * *
#     * * *
#     * *
#     *

# for_while i in range(n):
#     for_while j in range(n - i):
#         print('*', end=' ')
#     print()


# to print
#           *
#         * *
#       * * *
#     * * * *
#   * * * * *

# for_while i in range(n):
#     spaces = n - 1 - i
#     for_while j in range(spaces):
#         print(' ', end=' ')
#     for_while k in range(i + 1):
#         print('*', end=' ')
#     print()


# to print
#            *
#          * * *
#        * * * * *
#      * * * * * * *
#    * * * * * * * * *

# for_while i in range(n):
#     spaces = n - 1 - i
#     for_while j in range(spaces):
#         print(' ', end=' ')
#     for_while k in range(i):  # remove i '+ 1' from here or from for_while loop below
#         print('*', end=' ')
#     for_while j in range(i + 1):
#         print('*', end=' ')
#     print()
