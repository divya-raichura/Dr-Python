import os
import random

path_to_cat = "C:\\Users\\divya\\OneDrive\\Desktop\\CATS"  # path for the cats folder
os.chdir(path_to_cat)  # goes to the cats folder using above path

# there are 4 folders in cat, we want to choose one randomly
# print(os.listdir())  # prints the list of folders inside the current folder we are in
# we are in cats so, prints list with all 4 folders

folder_choice = random.choice(os.listdir(path_to_cat))  # args just for extra safety

# to go to that randomly chosen folder in above line we need that folder's path to do 'cd'
folder_choice_path = os.path.realpath(folder_choice)

# now, do cd into that folder as now you have path (was doing mistake here)
os.chdir(folder_choice_path)

# now you have videos, need to select one randomly
random_video = random.choice(os.listdir(folder_choice_path))
print('Enjoy Catzzzz')

# to play this randomly selected video :
# os.system("start " + random_video)
