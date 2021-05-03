import os

from fcrawler.utils     import _copy_file

class Crawler:
    def __init__(self, source_folder, desination_folder, file_type):
        self.src_folder = source_folder
        self.dst_folder = desination_folder
        self.file_type  = file_type
        self.listoffiles = list()

    def filelist(self):
        for (dirpath, _, filenames) in os.walk(self.src_folder):
            for filename in filenames:
                if filename.endswith(self.file_type):
                    self.listoffiles.append(os.path.join(dirpath, filename))

        return self.listoffiles

    def copy_files(self, custom_list=False, not_tree=False):
        if not custom_list:
            self.filelist()
        else:
            self.listoffiles = custom_list

        tot_files = len(self.listoffiles)
        count = 0
        print("\n")
        for file in self.listoffiles:
            count += 1
            _copy_file(file, self.dst_folder, not_tree, count, tot_files)
        print("\n")

def worker(src_folder=None, dst_folder=None, file_type=None, use_list=False, not_tree=False):
    app = Crawler(src_folder, dst_folder, file_type)

    if not use_list:
        app.copy_files(not_tree=not_tree)

    else:
        with open(use_list, "r") as txt_file:
            txt_lines = txt_file.readlines()

        index = 0
        for i in txt_lines:
            txt_lines[index] = i.replace("\n", "")
            index += 1

        app.copy_files(txt_lines, not_tree)

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
