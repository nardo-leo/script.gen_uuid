#!/usr/local/bin/python3


import pathlib
import uuid
import os


# rename files in path dir
def rename_files(path):
    files_counter = 0
    print(f'Rename files in {path}')
    # recursive go through all dirs and rename files
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            # if file not hidden and exclude script-file
            if not filename.startswith('.') and filename !=\
                   os.path.basename(__file__):
                # generate id and rename file
                id = uuid.uuid4()
                name = filename.split('.')
                new_name = name[0] + '_' + str(id) + '.' + name[1]
                os.rename(os.path.join(root, filename),
                          os.path.join(root, new_name))
                files_counter += 1
    print(f'{files_counter} files have been renamed')

    # remove script-file
    print("You don't ever need me. Buy... \n(x_x)")
    os.remove(__file__)


# get files in current dir
path = pathlib.Path(__file__).parent.absolute()
# and start rename func
rename_files(path)
