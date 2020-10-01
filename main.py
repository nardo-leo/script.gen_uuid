#!/usr/local/bin/python3


import pathlib
import uuid
import os


# rename files in path dir
def rename_files(path):
    for f in os.listdir(path):
        # if file not hidden and exclude script-file
        if not f.startswith('.') and f != 'main.py':
            # generate id and rename file
            id = uuid.uuid4()
            name = f.split('.')
            new_name = name[0] + '_' + str(id) + '.' + name[1]
            os.rename(f'{path}/{f}', f'{path}/{new_name}')
            print(f'{f} renamed')


# get files in current dir
path = pathlib.Path(__file__).parent.absolute()
# and start rename func
rename_files(path)
