import os
from os.path import isfile, join

# Defining a decorator that shows which function is currently running
def curent_function(func):
    def wrapper(*args, **kwargs):
        print(f'Function {func.__name__} started.')
        val = func(*args, **kwargs)
        print(f'Function {func.__name__} finished.')
        return val
    return wrapper

# Directory string needs to be seen as a raw string
def to_raw(dir):
    return fr'{dir}'

# Reading all files in a given directory
def read_all_files(dir):
    all_files = [f for f in os.listdir(dir) if isfile(join(dir, f))]

    return all_files

# Reading all existing directiories in a directory
def read_all_dirs(dir):
    all_dirs = [f for f in os.listdir(dir) if not isfile(join(dir, f))]
    
    return all_dirs

# Sorting files based on their type
@curent_function
def files_to_dict(all_files):
    files_dict = {}
    files_dict['TXTs'] = [f for f in all_files if f.endswith('.txt')]
    files_dict['PDFs'] = [f for f in all_files if f.endswith('.pdf')]
    files_dict['PHOTOS'] = [f for f in all_files if f.endswith(('.jpg', '.png', '.jpeg'))]
    #print(files_dict)
    return files_dict

# Checking if new directiories need to be created.
# The files will be sorted into 'PDFs', 'TXTs' and 'PHOTOS' directiories
# Creating new dirs for sorted files (if needed)
def create_dirs(files_dict, all_dirs, main_dir):
    new_dirs = []
    for key in files_dict.keys():
        if key not in all_dirs:
            new_dirs.append(key)

    if not new_dirs:
        return

    for dir in new_dirs:
        path = join(main_dir,dir)
        os.mkdir(path)

# Moving files into directories created by create_dirs
@curent_function
def sort_files(main_dir, files_dict):
    for key, files in files_dict.items():
        destination_dir = join(main_dir, key)
        if files:
            for f in files:
                os.rename(join(main_dir, f), join(destination_dir, f))

if __name__ == "__main__":
    #print("All files in directory: ", cleaning_dir)
    #print(read_all_files(cleaning_dir), "\n")
    #print("All dirs in directory: ", cleaning_dir) 
    #print(read_all_dirs(cleaning_dir))
    cleaning_dir = input("Directory to sort: ")
    cleaning_dir = to_raw(cleaning_dir)

    all_files = read_all_files(cleaning_dir)
    all_dirs = read_all_dirs(cleaning_dir)

    files_dict = files_to_dict(all_files)
    print(files_dict)
    create_dirs(files_dict, all_dirs, cleaning_dir)
    sort_files(cleaning_dir, files_dict)
    print("Done")

