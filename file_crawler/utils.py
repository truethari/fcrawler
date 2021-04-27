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

def _copy_file(source, destination, opt=1):
    if opt == 1:
        shutil.copy(source, destination)

    elif opt == 2:
        if destination.endswith('\\') or destination.endswith('/'):
            destination = destination[:-1]
        if destination.startswith('\\') or destination.startswith('/'):
            destination = destination[1:]

        full_path_destination = os.path.join(destination, os.path.dirname(source))
        os.makedirs(full_path_destination, exist_ok=True)
        shutil.copy(source , full_path_destination)
