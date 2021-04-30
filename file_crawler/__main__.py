import os
import sys
import optparse

from file_crawler.version           import __version__
from file_crawler.application       import worker

def _input_source_folder():
    current_folder = os.getcwd()
    while True:
        source_folder = input("Source folder\n: ") or None
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
        desination_folder = input("Desination folder\n: ") or None
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
            filelist_path = input("Specify a folder path to save the filelist.txt.\nPress Enter "
                                  "to save the filelist.txt to the current folder\n: ") or None
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
            filelist_path = input("Filelist (.txt) file path\nPress Enter to select a "
                                  "text file from the current folder\n: ") or None
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
                                filelist_path = os.path.join(current_folder, txt_files[txt_file_number - 1])
                                break
                        except ValueError:
                            print("Invalid number. Enter it again\n")
                            continue
                    break

        return filelist_path

def viewer():
    while True:
        try:
            user_input = int(input("[1] Copy files from a directory to another\n"
                                   "[2] Copy files from a directory to another "
                                   "(without creating subfolders)\n"
                                   "[3] Copy files using a filelist\n"
                                   "[4] Create filelist\n"
                                   "[5] Exit\n> "))
            if user_input == 1:
                pass
            elif user_input == 2:
                pass
            elif user_input == 3:
                pass
            elif user_input == 4:
                pass
            if user_input == 5:
                sys.exit()
            elif user_input > 5:
                print("Invalid input!")
                continue

        except ValueError:
            print("Invalid input!")
            continue
        except KeyboardInterrupt:
            sys.exit()

    ###not completed###

def main():
    usage = "usage: %prog [-s | --src] source_folder [-d | --dst] desination_folder \
            [-t | --type] file_type [options]"
    parser = optparse.OptionParser(description="FILE-CRAWLER v" + __version__, usage=usage)

    parser.add_option("-s", "--src",
            default=False,
            help="source folder"
            )
    parser.add_option("-d", "--dst",
            default=False,
            help="desination folder"
            )
    parser.add_option("-t", "--type",
            default=False,
            help="files type to crawl"
            )
    parser.add_option("-l", "--list",
            default=False,
            help="use files list"
            )
    parser.add_option("-f", "--file-list",
            default=False,
            help="generate files list file"
            )
    parser.add_option("-n", "--not-tree",
            action="store_true",
            default=False,
            help="don’t specify any sub directory"
            )
    parser.add_option("-v", "--version",
            action="store_true",
            default=False,
            help="show file-crawler version and exit"
            )
    (options, _) = parser.parse_args()
    options = vars(options)

    if options['version']:
        sys.exit(__version__)

    if options == {
                  'src': False,
                  'dst': False,
                  'type': False,
                  'list': False,
                  'file_list': False,
                  'not_tree': False,
                  'version': False
                  }:
        viewer()

    else:
        worker(options['src'], options['dst'], options['type'], options['list'],
               options['file_list'], options['not_tree'])

if __name__ == '__main__':
    main()
