import os
import sys
import pyfiglet

from fcrawler.application       import worker, create_filelist
from fcrawler.utils             import path_correction

def _input_source_folder():
    current_folder = os.getcwd()
    while True:
        source_folder = path_correction(input("Source folder\n: ") or None)
        if source_folder is not None:
            if not os.path.isdir(source_folder):
                print("source folder: '{}' No such directory. Enter it again.\n" \
                      .format(source_folder))
                continue
            else:
                break
        else:
            current_as_source = input("Do you want to use '{}' as the source folder? [Y/n]\n: " \
                                      .format(current_folder)) or 'y'
            if current_as_source.lower() == 'y':
                source_folder = current_folder
                break
            else:
                sys.exit()

    return source_folder

def _input_desination_folder(source_folder=None):
    current_folder = os.getcwd()
    while True:
        desination_folder = path_correction(input("Desination folder\n: ") or None)
        if desination_folder is not None:
            if not os.path.isdir(desination_folder):
                print("desination folder: '{}' No such directory. Enter it again.\n." \
                      .format(desination_folder))
                continue
            else:
                break
        else:
            if current_folder != source_folder:
                current_as_destination = input("Do you want to use '{}' as the desination folder? "
                                               "[Y/n]\n: ".format(current_folder)) or 'y'
                if current_as_destination.lower() == 'y':
                    desination_folder = current_folder
                    break
                elif current_as_destination.lower() == 'n':
                    sys.exit()
            else:
                print("Enter a valid path to the destination folder.\n")

    return desination_folder

def _input_filelist(option="create"):
    current_folder = os.getcwd()
    if option == "create":
        while True:
            filelist_path = path_correction(input("Specify a folder path to save the filelist.txt. "
                            "Press Enter to save the filelist.txt to the current folder\n: ") or None)
            if filelist_path is None:
                filelist_path = current_folder
                break
            else:
                if not os.path.isdir(filelist_path):
                    print("filelist path: '{}' No such directory. Enter it again.\n" \
                          .format(filelist_path))
                    continue
                else:
                    break

    elif option == "input":
        txt_files = []
        while True:
            filelist_path = path_correction(input("Filelist (.txt) file path. Press Enter to "
                                            "select a text file from the current folder\n: ") or None)
            if filelist_path is not None:
                if not os.path.isfile(filelist_path):
                    print("filelist path: '{}' No such text file. Enter it again.\n" \
                          .format(filelist_path))
                    continue
                elif not filelist_path.endswith(".txt"):
                    print("filelist path: '{}' invalid text file. Enter it again.\n" \
                          .format(filelist_path))
                    continue
                else:
                    break
            else: # if filelist_path is None
                for file in os.listdir(current_folder):
                    if file.endswith(".txt"):
                        txt_files.append(file)

                if len(txt_files) == 0:
                    print("No text file found in this folder!\n")

                else:
                    count = 0
                    for file in txt_files:
                        count += 1
                        print("[{}] {}".format(count, file))

                    while True:
                        try:
                            txt_file_number = int(input("Enter the text file number\n> "))
                            if txt_file_number > len(txt_files) or txt_file_number == 0:
                                raise ValueError
                            else:
                                filelist_path = os.path.join(current_folder,
                                                txt_files[txt_file_number - 1])
                                break
                        except ValueError:
                            print("Invalid number. Enter it again\n")
                            continue
                    break

    return filelist_path

def _input_type():
    return input("File type (Ex: .mp4, .zip)\n: ")

def main():
    while True:
        try:
            print(pyfiglet.figlet_format("FCrawler"))
            user_input = int(input("[1] Copy files from a directory to another\n"
                                   "[2] Copy files from a directory to another "
                                   "(without creating subfolders)\n"
                                   "[3] Copy files using a filelist\n"
                                   "[4] Create filelist\n"
                                   "[5] Exit\n> "))
            if user_input == 1:
                source_folder = _input_source_folder()
                file_type = _input_type()
                desination_folder = _input_desination_folder()
                worker(source_folder, desination_folder, file_type, tree=True)

            elif user_input == 2:
                source_folder = _input_source_folder()
                file_type = _input_type()
                desination_folder = _input_desination_folder()
                worker(source_folder, desination_folder, file_type, tree=False)

            elif user_input == 3:
                filelist = _input_filelist("input")
                desination_folder = _input_desination_folder()
                worker(dst_folder=desination_folder, use_list=filelist)

            elif user_input == 4:
                source_folder = _input_source_folder()
                file_type = _input_type()
                save_path = _input_filelist()
                create_filelist(source_folder, file_type, save_path)
                print("\n")

            if user_input == 5:
                sys.exit()
            elif user_input > 5:
                raise ValueError

        except ValueError:
            print("Invalid input!\n")
            continue
        except KeyboardInterrupt:
            sys.exit()

if __name__ == '__main__':
    main()
