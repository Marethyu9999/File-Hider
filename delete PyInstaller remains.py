import os
import shutil

dir_path = os.path.dirname(os.path.realpath(__file__))
rmv = ["{0}/dist".format(dir_path), "{0}/build".format(dir_path), "{0}/main.spec", "{0]/__pycache__"]


def file_check(checking):
    isfile = os.path.isfile(checking)
    isdir = os.path.isdir(checking)
    if isfile:
        return "IsFile"
    elif isdir:
        return "IsDir"


for x in rmv:
    if file_check(x) == "IsFile":
        os.remove(x)
        print("Removed file: {0}".format(x))
    elif file_check(x) == "IsDir":
        shutil.rmtree(x)
        print("Removed Directory: {0}".format(x))

input("... ")
exit()
