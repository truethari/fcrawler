import os
import sys
import shutil

from fcrawler.utils     import _copy_file

class Crawler:
    def __init__(self, source_folder, desination_folder, file_type):
        self.src_folder = source_folder
        self.dst_folder = desination_folder
        self.file_type  = file_type
        self.listoffiles = list()

    def filelist(self):
        files = 0
        sys.stdout.write("Hold on. This will take some time")
        sys.stdout.flush()
        os_walk = os.walk(self.src_folder)
        for (dirpath, _, filenames) in os_walk:
            for filename in filenames:
                if filename.endswith(self.file_type):
                    files += 1
                    sys.stdout.write('\r')
                    sys.stdout.write("{} files of '{}' file type were found."
                                     .format(files, self.file_type))
                    sys.stdout.flush()
                    self.listoffiles.append(os.path.join(dirpath, filename))

        return self.listoffiles

    def check_free_space(self, filelist):
        total_size = 0
        status = True
        for file in filelist:
            total_size += os.path.getsize(file)

        if total_size > shutil.disk_usage(self.dst_folder)[2]:
            user_input = input("\nThere is not enough space on the destination drive.\nCopy anyway? [Y/n]\n") or "y"
            if user_input.lower() != 'y':
                status = False

        return status

    def copy_files(self, custom_list=False, tree=True):
        if not custom_list:
            self.filelist()
        else:
            self.listoffiles = custom_list

        if self.check_free_space(self.listoffiles):
            count = 0
            tot_files = len(self.listoffiles)
            for file in self.listoffiles:
                count += 1
                _copy_file(file, self.dst_folder, tree, count, tot_files)

def worker(src_folder=None, dst_folder=None, file_type=None, use_list=False, tree=True):
    app = Crawler(src_folder, dst_folder, file_type)

    if not use_list:
        app.copy_files(tree=tree)

    else:
        with open(use_list, "r") as txt_file:
            txt_lines = txt_file.readlines()

        index = 0
        for i in txt_lines:
            txt_lines[index] = i.replace("\n", "")
            index += 1

        app.copy_files(txt_lines, tree)

def create_filelist(source_folder, file_type, save_path):
    app = Crawler(source_folder, None, file_type)
    filelist = app.filelist()
    text_file = open(os.path.join(save_path, "filelist.txt"), "a")
    for filename in filelist:
        try:
            text_file.write(filename + '\n')
        except UnicodeEncodeError:
            pass
    text_file.close()

    return True
