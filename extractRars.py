import shutil
<<<<<<< HEAD

import fnmatch
import os
import sys
exten = ['*01.rar']
if len(sys.argv) != 2:
    print ('Use extactrars and input folder as argument.')
else:
    for root, dirs, files in os.walk(sys.argv[1]):
        for extensions in exten:
             for fi in files:
                 print (fi)
                 print (extensions)
		 if fi.endswith(extensions):
            print("extracting: "+ fi)
            os.system("unrar e \"" + os.path.join(root, fi)+"\"")
=======
import fnmatch
import os
exten = ['*01.rar']
for root, dirs, files in os.walk("/media/Seagate Expansion Drive/guest/Series/24 Horas"):
    for extensions in exten:
        for files in fnmatch.filter(files, extensions):
            print("extracting: "+ files)
            os.system("unrar x \"" + os.path.join(root, files)+"\"")
>>>>>>> origin/master


