# -*- coding: utf-8 -*-
#----------------------------------------------------------
# move_new.py
#
# Created by: Mikel Frutos 2014
#
# A simple program that process finished Transmission torrents 
# and move from download folder to NAS specific folder, renaming 
# special characters and removing empty folder from origin
#----------------------------------------------------------


import json
import os
from pprint import pprint
import os, subprocess
from shutil import move
from shutil import copy2
from shutil import rmtree
import codecs

from transmissionTools import clearTrans


# test for video files to move
def isVid(name):
    if ".mkv" in name:
        return True    
    if ".avi" in name:
        return True
    if ".mp4" in name:
        return True
    return False


#move from usb download folder to NAS destination folder
def moveto(ddir,udir, fold):
    print("---------------------Moving-----------------------" )
    for filemask in fold:
        for root, dirs, files in os.walk(ddir):   #.encode("ISO-8859-2")):
            encontrado = False
            for name in files:
                if isVid(name):
                    if filemask["id"] in name: # in my_utf8:
                        encontrado = True
                        print (name)
                        dst1 = os.path.join(udir,filemask["value"])
                        dst = os.path.join(dst1,name) #.decode("ISO-8859-2"))
                        src = os.path.join(root, name) #.decode("ISO-8859-2")) 
                        try:
                            print "Removing video %s" % (src)
                            move( src, dst) #.encode("ISO-8859-2"), dst.encode("ISO-8859-2"))
                        except: 
                            print "Oops! no se ha podido mover."
                 

# Main function
def main():
    with open('data.json') as data_file:    
        data = json.load(data_file)
        folders = data["folder"]
        downdir = data["downloads_dir"]
        updir = data["upload_dir"]
    moveto(downdir, updir, folders)


main()
