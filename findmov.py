# -*- coding: utf-8 -*-
import shutil
import fnmatch
import os
movies = ['*.mov','*.MOV','*.mkv', '*.MKV']
for root, dirs, files in os.walk("/media/Seagate Expansion Drive/guest/fotos"):
    for extensions in movies:
        for files in fnmatch.filter(files, extensions):
             path = root.replace('fotos','videos')
	     if not os.path.exists(path):
                 os.makedirs(path)
                 print(path)
             shutil.move(os.path.join(root, files),path)
             print(os.path.join(root, files))
     
    
