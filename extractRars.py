import shutil
import fnmatch
import os
exten = ['*01.rar']
for root, dirs, files in os.walk("/media/Seagate Expansion Drive/guest/Series/24 Horas"):
    for extensions in exten:
        for files in fnmatch.filter(files, extensions):
            print("extracting: "+ files)
            os.system("unrar x \"" + os.path.join(root, files)+"\"")


