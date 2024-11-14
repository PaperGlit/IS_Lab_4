import shutil
import os


def remove_temp():
    if not os.path.exists("temp/"):
        os.mkdir("temp/")

    for i in os.listdir("temp/"):
        item = os.path.join("temp/", i)
        if os.path.isdir(item):
            shutil.rmtree(item)
        elif os.path.isfile(item):
            os.remove(item)