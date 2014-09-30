import shutil
import fnmatch
import os
import sys
exten = ['.7z']
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
                       os.system("7za e \"" + os.path.join(root, fi)+"\"")
                       #os.system("7za e \"" + os.path.join(root, fi)+"\" -o \""+root+"\"")


