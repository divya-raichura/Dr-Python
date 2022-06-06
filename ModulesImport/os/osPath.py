import os

# os.path.join used to combine

print(os.path.basename('\\tmp\\test.txt'))
print(os.path.dirname('\\tmp\\test.txt'))
print(os.path.split('\\tmp\\test.txt'))
print(os.path.exists('\\tmp\\test.txt'))

# sometimes names are like 'fafeegsa' or something random
# to know if it is dir or file we use os.path.isdir or os.path.isfile
# gives boolean value


print(os.path.splitext('\\tmp\\test.txt'))  # it separates extension and root name


print(dir(os.path))



