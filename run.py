import os
from os.path import isfile, join

# Directory that needs to be sorted
cleaning_dir = r'C:\Users\migro\Desktop'

# Reading all files in a given directory
def read_all_files(dir):
    all_files = [f for f in os.listdir(dir) if isfile(join(dir, f))]

    return all_files

# Reading all existing directiories in a directory
def read_all_dirs(dir):
    all_dirs = [f for f in os.listdir(dir) if not isfile(join(dir, f))]
    
    return all_dirs

# Sorting files based on their type
def files_to_dict(all_files):
    files_dict = {}
    files_dict['TXTs'] = [f for f in all_files if f.endswith('.txt')]
    files_dict['PDFs'] = [f for f in all_files if f.endswith('.pdf')]
    files_dict['PHOTOS'] = [f for f in all_files if f.endswith(('.jpg', '.png', '.jpeg'))]

    return files_dict

# Checking if new directiories need to be created.
# The files will be sorted into 'PDFs', 'TXTs' and 'PHOTOS' directiories
# Creating new dirs for sorted files (if needed)
def create_dirs(files_dict, dirs, main_dir):
    new_dirs = []
    for key in files_dict:
        if key not in dirs:
            new_dirs.append(key)

    for dir in new_dirs:
        path = join(main_dir,dir)
        os.mkdir(path)



if __name__ == "__main__":
    #print("All files in directory: ", cleaning_dir)
    #print(read_all_files(cleaning_dir), "\n")
    #print("All dirs in directory: ", cleaning_dir) 
    #print(read_all_dirs(cleaning_dir))

    all_files = read_all_files(cleaning_dir)
    all_dirs = read_all_dirs(cleaning_dir)

    files_dict = files_to_dict(all_files)
    create_dirs(files_dict, all_dirs, cleaning_dir)

    print("Done")

