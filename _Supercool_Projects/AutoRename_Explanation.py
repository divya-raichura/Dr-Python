# we want to change a file name from
# "Earth - The Solar System - # 3.txt"
# to
# "# 3 - Earth - The Solar System.txt"
# so that all files are number wise

import os

os.chdir('C:\\Users\\divya\\solarsystem')

for f in os.listdir():
    # print(f)
    # print(os.path.splitext(f))  # gives tuple containing name and its extension
    file_name, file_extn = os.path.splitext(f)
    # print(file_name)
    # we can split at hypens
    # print(file_name.split(' - '))  # gives a list with 3 indexes which we can store in 3 vars
    f_title, f_course, f_num = file_name.split('-')
    # if we have weird spaces we can do  # we can do split(' - ') in this case
    # so no prob in this case but for other situation it may not possible so we use below approach

    f_title = f_title.strip()
    f_course = f_course.strip()
    # f_num = f_num[3:]  # or we can strip and do remove '#' together
    f_num = f_num.strip()[2:]

    # print(f'{f_num}-{f_title}-{f_course}{file_extn}')
    # now prob is '1' and '10' will be like '1' and after that '10'
    # to solve this we can put 0 before everyone so that '01' ke bad '02' aaye not '10'
    # we can do this using zfill(no of digits) method which converts an integer
    # to the no of digits we pass in by applying leading zeroes to it
    f_num = f_num.zfill(2)
    # print(f'{f_num}-{f_title}-{f_course}{file_extn}')
    # we can also remove course name as it is no good looking
    # print(f'{f_num}-{f_title}{file_extn}')
    new_name = f'{f_num}-{f_title}{file_extn}'

    # original file name is 'f' as we see in for loop, we can rename it to above name using
    os.rename(f, new_name)



