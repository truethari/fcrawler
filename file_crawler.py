"""
File Crawler

For test purposes only.
"""

import os
import shutil
import sys
import pathlib

def _list_of_files(directory, extention):
    listoffiles = list()
    for (dirpath, dirnames, filenames) in os.walk(directory):
        for filename in filenames:
            if filename.endswith(extention):
                listoffiles.append(os.path.join(dirpath, filename))

    return listoffiles

def _txt_list_of_files(txt_filepath):
    with open(txt_filepath, "r") as txt_file:
        txt_lines = txt_file.readlines()

    possiiton = 0
    for i in txt_lines:
        txt_lines[possiiton] = i.replace("\n", "")
        possiiton += 1

    return txt_lines

def _convert_bytes(size_in_bytes, unit='MB'):
    if unit == 'KB':
        size = round((size_in_bytes/1024), 2)
    elif unit == 'MB':
        size = round(size_in_bytes/(1024*1024), 2)
    elif unit == 'GB':
        size = round(size_in_bytes/(1024*1024*1024), 2)
    else:
        size = size_in_bytes

    return size

def _copy_file(source, destination):
    shutil.copy(source, destination)

def _input_source_folder():
    loop_source_folder = True
    while loop_source_folder:
        source_folder = str(input("path: ") or 0)

        if source_folder == '0':
            source_folder = str(pathlib.Path(__file__).parent.absolute())
            print('{} use as the source folder!'.format(source_folder))
            loop_source_folder = False
        
        elif not os.path.exists(source_folder):
            print("No folder found! Enter path again!")
        
        elif os.path.exists(source_folder):
            loop_source_folder = False
    
    return source_folder

def _input_destination_folder():
    while True:
        destination_folder = str(input("dest: ") or 0)

        if destination_folder == '0':
            destination_folder = str(pathlib.Path(__file__).parent.absolute())
            print('{} use as the destination folder!'.format(destination_folder))
            break

        elif not os.path.exists(destination_folder):
            print("No folder found! Enter path again!")

        elif os.path.exists(destination_folder):
            break

    return destination_folder

def _input_file_extention():
    while True:
        file_extention = str(input("extention: ") or 0)
        if file_extention == '0':
            print("Please enter a file extention! Ex: .mp4, .mp3")
        else:
            break

    return file_extention

def _input_txt_path():
    while True:
        txt_path = str(input("Txt path: ") or 0)
        if txt_path == '0':
            print("Please enter a txt path!")

        else:
            break

    return txt_path

def _file_size(file_path):
    size = os.path.getsize(file_path)
    return size

def _file_list_size(file_list):
    list_size = 0
    for i in file_list:
        list_size += _file_size(i)

    return _convert_bytes(list_size)

def _file_list_to_txt(folder, content):
    f = open(os.path.join(folder, "filelist.txt"), "a")
    try:
        f.write(content + '\n')
    except UnicodeEncodeError:
        pass
    f.close()

def main():
    main_loop = True
    while main_loop:
        method = int(input("  [1] Create filelist.txt\n"\
                        "  [2] Copy files using filelist.txt\n"\
                        "  [3] Create filelist and Copy Files\n"\
                        "  [4] Exit\n"))

        if method == 1:
            source_folder = _input_source_folder()
            file_extention = _input_file_extention()

            list_of_files = _list_of_files(source_folder, file_extention)

            for i in list_of_files:
                _file_list_to_txt(pathlib.Path(__file__).parent.absolute(), i)

        elif method == 2:
            destination_folder = _input_destination_folder()
            txt_path = _input_txt_path()
            print("Size = {}MB".format(_file_list_size(_txt_list_of_files(os.path.join(destination_folder, txt_path)))))
            user_action = str(input("Do you want to continue? [Y/n]\n"))
            if user_action in ('n', 'N'):
                sys.exit()
            elif user_action in ('y', 'Y'):
                pass

        else:
            sys.exit()

if __name__ == '__main__':
    main()