import PyInstaller.__main__
import time
import shutil
import os

PyInstaller.__main__.run([
    'main.py',
])

src = "path/dist/main/main.exe"
dst = "path"

shutil.copy2(src, dst)

waiting_time = 3

while waiting_time > 0:
    time.sleep(1)
    print("Waited 1 out of {0} seconds".format(waiting_time))
    waiting_time = - 1

rmv = ["path/dist", "path/build", "path/__pycache__", "main.spec"]

for x in rmv:
    os.remove(x)
    print("{0} wurde gelöscht.".format(x))

input("... ")