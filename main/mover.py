import glob
import shutil
import os

extracted_folder = 'extracted/'
downloaded_folder = 'downloaded/'


def move_to(target_dir):
    files = glob.glob(extracted_folder + '*site.xml')
    for file in files:
        if os.name == 'posix':
            separator = '/'
        else:
            separator = '\\'
        file_name = file.split(separator)[1]
        shutil.move(file, target_dir + file_name)
        print(file_name + ' moved')


def flush():
    files = glob.glob(extracted_folder + '*')
    for file in files:
        os.remove(file)
        print(file + ' removed')

    files = glob.glob(downloaded_folder + '*')
    for file in files:
        os.remove(file)
        print(file + ' removed')
