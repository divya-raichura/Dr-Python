# https://www.javatpoint.com/python-files-io
# if file opened in read mode & it doesn't exist & we try to read it, then file not found exception

# a = open("yeFileHai.txt", "w")  # creates new file if no file exists
# same with "a"
# content = a.write("hello")
# print(content)  # prints no of chars since write mode khola
# a.close()

# with open("yeFileHai.txt", "r") as a:
#     content = a.read()
#     print(content)

# a = open("yeFileHai.txt", "a")
# a.write(" world")
# a.close()

# a = open("yeFileHai.txt", "r")
# # a.read()  # this reads whole file
# content = a.read(5)  # this reads the number of chars
# print(type(content))
# print(content)
# a.close()

# a = open("yeFileHai.txt", "r")
# for i in a:
#     print(i)  # 'i' contains each line of the file
#
# content1 = a.readlines()
# content2 = a.readlines()
# print(content1)
# print(content2)

# a = open("yeFileHai.txt", "w")  # w over writes on the file, if we
# want to add content to file, we need to use 'a' -> append
# a.write("I am elon musk") a.close()
#
# a = open("yeFileHai.txt", "r")
# print(a.read())
#
# a = open("nayaFileToTest", "w")
# a.write("""To test if we write to file that doesn't exist then it will make new one and write in it or not?
# If this file exists then the ans is Yes""")
# a.close()
# a = open("nayaFileToTest", "r")
# print(a.readlines())
# a.close()
