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


# rename especial charactrers from folders name
def renamedir(mydir):
    print("---------------------Renaming-----------------------" )
    for fn in os.listdir(mydir):
        renombrar = False
        src = os.path.join(mydir, fn.decode("ISO-8859-2"))
        newDirName = ""
        for index, item in enumerate(fn):
            if item.encode('hex') == "c3" :
                newDirName=newDirName+"_"
                renombrar = True
            elif item.encode('hex') == "b1" :
                newDirName=newDirName+"_"
                renombrar = True
            else:
                newDirName=newDirName+item
        if renombrar:
            dst = os.path.join(mydir, newDirName)
            renombrar = False
            print(dst)
            os.rename(src.encode("ISO-8859-2"), dst)


# move from usb download folder to NAS destination folder
def moveto(ddir,udir, fold):
    print("---------------------Moving-----------------------" )
    for filename in os.listdir(ddir):
        for filemask in fold:
            #my_utf8 = filename.decode("ISO-8859-2")
            if filemask["id"] in filename: # in my_utf8:
                fullpath = ddir+"/"+ filename #my_utf8
                for root, dirs, files in os.walk(fullpath):   #.encode("ISO-8859-2")):
                    encontrado = False
                    for name in files:
                        if isVid(name):
                            encontrado = True
                            print (name)
                            dst1 = os.path.join(udir,filemask["value"])
                            dst = os.path.join(dst1,name) #.decode("ISO-8859-2"))
                            src = os.path.join(root, name) #.decode("ISO-8859-2"))
                            try:
                                move( src, dst) #.encode("ISO-8859-2"), dst.encode("ISO-8859-2"))
                                if not os.path.isfile(src):
                                    try:
                                        print "Removing video........"
                                        #rmtree(root,ignore_errors=True)
                                        break
                                    except:
                                        print "Oops! no se ha podido borrar."
                            except (OSError, IOError), e:
                                    print 'Error moving %s to %s: %s' % (src.encode("ISO-8859-2"), dst.encode("ISO-8859-2"), e)
                    if not encontrado:
                        try:
                            print "Borrando no encontrado ........"
                            #rmtree(root,ignore_errors=True)
                        except:
                            print "Oops! no se ha podido borrar."

        print "-------------------------------------------------------------"


# Main function
def main():
    clearTrans()
    with open('data.json') as data_file:    
        data = json.load(data_file)
        folders = data["folder"]
        downdir = data["downloads_dir"]
        updir = data["upload_dir"]
    #renamedir(downdir)
    moveto(downdir, updir, folders)


main()
