import os
import sys
import optparse

from file_crawler.version           import __version__
from file_crawler.application       import worker

def _input_source_folder():
    current_folder = os.getcwd()
    while True:
        source_folder = input("Source folder: ") or None
        if source_folder is not None:
            if not os.path.isdir(source_folder):
                print("source folder: {} No such directory. Enter it again.".format(source_folder))
                continue
            else:
                break
        else:
            current_as_source = input("Do you want to use {} \
                                       as the source folder? [Y/n]\n".format(current_folder)) or 'n'
            if current_folder.lower() == 'y':
                source_folder = current_folder
                break
            else:
                sys.exit()

    return source_folder

def _input_desination_folder(source_folder=None):
    while True:
        desination_folder = input("Desination folder: ") or None
        if desination_folder is not None:
            if not os.path.isdir(desination_folder):
                print("desination folder: {} No such directory. Enter it again.".format(desination_folder))
                continue
            else:
                break
        else:
            if current_folder != source_folder:
                current_as_destination = input("Do you want to use {} \
                                                as the desination folder? [Y/n]\n".format(current_folder)) or 'n'
                if current_folder.lower() == 'y':
                    desination_folder = current_folder
                    break
            else:
                print("Enter a valid path to the destination folder.")

def viewer():
    while True:
        try:
            user_input = int(input("[1] Copy files from directory(tree) to directory\n"
                                   "[2] Copy files from directory(not tree) to directory\n"
                                   "[3] Copy files using a filelist\n"
                                   "[4] Create filelist\n"
                                   "[5] Exit"))
            if user_input == 5:
                sys.exit()
            elif user_input > 5:
                print("Invalid input!")
                continue
            else:
                break

        except ValueError:
            print("Invalid input!")
            continue

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
        pass

    else:
        worker(options['src'], options['dst'], options['type'], options['list'],
               options['file_list'], options['not_tree'])

if __name__ == '__main__':
    main()
