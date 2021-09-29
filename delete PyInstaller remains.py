# Importing modules
import os
import shutil

# Defining Paths
dir_path = os.path.dirname(os.path.realpath(__file__))
copy_exe_src = "{0}/dist/main.exe".format(dir_path)
rmv = ["{0}/dist".format(dir_path), "{0}/build".format(dir_path), "{0}/main.spec".format(dir_path),
       "{0}/__pycache__".format(dir_path)]

# Copying main.exe to active
shutil.copy2(copy_exe_src, dir_path)
print("{0} was copied to the active directory.".format(copy_exe_src))


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
    else:
        print("Something is not working!\nx={0}".format(x))

input("... ")
exit()
