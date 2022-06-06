import os
from datetime import datetime
os.chdir('C:\\Users\\divya\\OneDrive\\Desktop')
# os.mkdir('demo.txt')
# print(os.listdir())
mod = os.stat('demo.txt')
# print(mod)

# st_mtime is time when file was modified
# st_size is size of file
mod_time = os.stat('demo.txt').st_mtime
# print(mod_time)  # 1654057740.4019282 --> not readable
# print(datetime.fromtimestamp(mod_time))

# for dirpath, dirname, filename in os.walk('C:\\Users\\divya\\OneDrive\\Desktop'):
#     print('Current path: ', dirpath)
#     print('Directories: ', dirname)
#     print('Files: ', filename)
#     print()




