import uuid
import os
import sys


# rename files in path dir
def rename_files(path):
    for f in os.listdir(path):
        # if not hidden
        if not f.startswith('.'):
            print(f'{f} renamed')
            # generate id and rename file
            id = uuid.uuid4()
            name = f.split('.')
            new_name = name[0] + '_' + str(id) + '.' + name[1]
            os.rename(f, new_name)


# get path from param
path = sys.argv[1]
rename_files(path)
