import os

folder_path = "C:\\Users\\divya\\Dr-Java-DSA\\src\\dynamic " \
              "programming\\src\\com\\company\\dp\\lecs_tuf"

os.chdir(folder_path)

folders = os.listdir()

folders.pop()

for folder in folders:
    os.chdir(folder_path + f'\\{folder}')
    files = os.listdir()
    for file in files:
        name, ext = file.split('.')
        empty, lec_no, lec_name = name.split('_')
        new_name = f'L{lec_no}_{lec_name}.{ext}'
        os.rename(file, new_name)