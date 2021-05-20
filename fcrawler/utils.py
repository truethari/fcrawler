import os
import shutil

def _convert_bytes(size_in_bytes, unit='MiB'):
    if unit == 'KiB':
        size = round((size_in_bytes/1024), 2)
    elif unit == 'MiB':
        size = round(size_in_bytes/(1024*1024), 2)
    elif unit == 'GiB':
        size = round(size_in_bytes/(1024*1024*1024), 2)
    elif unit == 'TiB':
        size = round(size_in_bytes/(1024*1024*1024*1024), 2)

    return size

def _copy_file(source, destination, tree, counter=0, total=0):
    if tree:
        tmp_source = source
        if tmp_source.endswith('\\') or tmp_source.endswith('/'):
            tmp_source = tmp_source[:-1]
        if tmp_source.startswith('\\') or tmp_source.startswith('/'):
            tmp_source = tmp_source[1:]
        if ":" in tmp_source:
            tmp_source = tmp_source.replace(":", "")

        full_path_destination = os.path.join(destination, os.path.dirname(tmp_source))
        os.makedirs(full_path_destination, exist_ok=True)
        if os.path.isfile(os.path.join(full_path_destination, os.path.basename(source))):
            print("Skipped: {:<100}\t{:<10}".format(source, (str(counter) + "/" + str(total))))
        else:
            shutil.copy(source , full_path_destination)
            print("Copied: {:<100}\t{:<10}".format(source, (str(counter) + "/" + str(total))))

    elif not tree:
        if os.path.isfile(os.path.join(destination, os.path.basename(source))):
            print("Skipped: {:<100}\t{:<10}".format(source, (str(counter) + "/" + str(total))))
        else:
            shutil.copy(source, destination)
            print("Copied: {:<100}\t{:<10}".format(source, (str(counter) + "/" + str(total))))

def path_correction(path):
    if path is not None:
        if path.startswith("'") or path.startswith("\""):
            path = path[1:]
        if path.endswith("'") or path.endswith("\""):
            path = path[:-1]

    return path
