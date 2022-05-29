# f = open("fileRevise.txt", 'r')
#
# print(f.name)
# print(f.mode)
#
# f.close()

# using context managers
# why best? automatically closes file
# closes file even if exceptions are thrown

# with open("fileRevise.txt", 'r') as f:
#     f_contents = f.read()
#     print(f_contents)

# read reads entire content at once but we can specify no of words
# nextLine reads a new line everytime we run it
# with open("fileRevise.txt", 'r') as f:
    # for line in f:  # this reads one line at a time in each iteration
    #     # so it is memory efficient
    #     print(line, end='')

    # f_contents = f.readline()
    # print(f_contents, end='')
    # f_contents = f.readline()
    # print(f_contents, end='')

    # f_contents = f.read(10)  # when we run it again, it will
    # start from the point where it left
    # print(f_contents)

# how to read large files using 'read'
with open("fileRevise.txt", 'r') as f:
    sizeToRead = 10
    f_contents = f.read(sizeToRead)
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(sizeToRead)

# f.tell() gives the position of the cursor and
# we can manipulate it using f.seek()

