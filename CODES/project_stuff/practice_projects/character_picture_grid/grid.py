grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

# this prints the list elements above as simple strings
# for_while row in grid:
#     for_while col in row:
#         print(col, end=' ')
#     print()


# this is also like above code
# for_while index, value in enumerate(grid):
#     for_while index_c, value_c in enumerate(value):
#         print(grid[index][index_c], end=' ')
#     print()


for i in range(6):  # 6 --> length of inner list(no of cols)
    for j in range(9):  # 9 --> length of outer list(no of rows)
        print(grid[j][i], end=' ')
    print()
