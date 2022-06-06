
import os

print(dir(os))

print(os.getcwd())
os.chdir('C:\\Users\\divya\\OneDrive\\Desktop')
print(os.getcwd())
print(os.listdir())
# os.mkdir('Os_demo_dir')
# os.mkdir('Os_demo_dir/Sub_dir')  # not possible to create subdir
# to do it we use :-
# os.makedirs()
print(os.listdir())
# os.rmdir('Os_demo_dir')
print(os.listdir())
print(os.stat('CATS'))
