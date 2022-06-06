import os

os.chdir('C:\\Users\\divya\\solarsystem')

for f in os.listdir():
    file_name, file_extn = os.path.splitext(f)

    f_title, f_course, f_num = file_name.split('-')

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[2:].zfill(2)

    new_name = f'{f_num}-{f_title}{file_extn}'

    os.rename(f, new_name)


