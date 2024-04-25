import os
import shutil

file_extension = {
    'pdf': 'PDFs',
    'png': 'PNGs',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Images',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'csv': 'Data',
    'xlsx': 'Data',
    'zip': 'Archives',
    'rar': 'Archives',
    'exe': 'Executables',
    'mp3': 'Music',
    'wav': 'Music',
    'mp4': 'Videos',
    'avi': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos',
    'mov': 'Videos'
}

targetDir = 'C:/Users/Daniel/Desktop'

with os.listdir(path=targetDir) as dir:
    print(type(dir))
    for item in dir:
        print(type(item))
    # for item in dir:
    #     type = file_extension.get(item.name.split('.')[-1]);
    #     print(item)
    #     print(type)
        # if item.name.endswith()
        # shutil.move(f'C:/Users/Daniel/Desktop/{item.name}', f'C:/Users/Daniel/Desktop/{type}')
        # print(item)
