# c3_52_p2.pdf/dwg

import os

os.chdir('C:\\Users\\divya\\renameThis')

for f in os.listdir():
    file_name, file_extn = os.path.splitext(f)
    newFileNameStarter = "C3_52"
    # v4:iso model v1:roll v2:surname v3:ps-model
    roll, sur, ps_model, *v4 = file_name.split('_')
    ps, *model = ps_model.split(' - ')

    newName = f'{newFileNameStarter}_{ps}{file_extn}'
    os.rename(f,newName)
