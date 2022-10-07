import os

path = "C:\\Users\\divya\\spit\\sem3"
os.chdir(path)

folders = os.listdir()

for folder in folders:
    folderPath = path + "\\" + folder
    os.chdir(folderPath)
    folderFiles = os.listdir()
    for file in folderFiles:
        fileName, ext = file.split('.')
        newName = "Syllabus" + "." + ext
        os.rename(file, newName)

    os.chdir(path)
