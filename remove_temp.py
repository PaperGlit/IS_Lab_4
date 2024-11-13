import shutil
import os


def remove_temp(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

    for i in os.listdir(directory):
        item = os.path.join(directory, i)
        if os.path.isdir(item):
            shutil.rmtree(item)
        elif os.path.isfile(item):
            os.remove(item)