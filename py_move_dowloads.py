import json
import os
from pprint import pprint
import os, subprocess
from shutil import move
from shutil import copy2
from shutil import rmtree
import codecs

with open('data.json') as data_file:    
    data = json.load(data_file)
    folders = data["folder"]
for filename in os.listdir(data["downloads_dir"]):
	for filemask in folders:
		my_utf8 = filename.decode("ISO-8859-2")
		if filemask["id"] in my_utf8:
			#print("-------------------  %s",my_utf8)
			fullpath = data["downloads_dir"]+"/"+my_utf8
			#fullpath = data["downloads_dir"]+"/"+filename
			for root, dirs, files in os.walk(fullpath.encode("ISO-8859-2")):
				for name in files:
					encontrado = False
					if "mkv" in name:
						encontrado = True
						print "uploading " + name
						dst1 = os.path.join(data["upload_dir"],filemask["value"])
						dst = os.path.join(dst1,name.decode("ISO-8859-2"))
						print os.getcwd()    
						#os.chdir(dst)
						#print os.getcwd() 
						src = os.path.join(root, name.decode("ISO-8859-2"))
						#src = root +"/"+ name
						print src.encode("ISO-8859-2")
						try:
 							move( src.encode("ISO-8859-2"), dst.encode("ISO-8859-2"))
							if not os.path.isfile(src):
								try:
									print "Borrando........"
									#rmtree(root,ignore_errors=True)
								except:
									print "Oops! no se ha podido borrar."
						except (OSError, IOError), e:
        						print 'Error moving %s to %s: %s' % (src.encode("ISO-8859-2"), dst.encode("ISO-8859-2"), e)
					if "avi" in name:
						encontrado = True
						print "uploading " + name
						src = root +"/"+ name
						dst = data["upload_dir"]+"/"+filemask["value"]+"/"+name
						try:
 							move( src, dst)
							if not os.path.isfile(src):
								try:
									print "Borrando........"
									#rmtree(root,ignore_errors=True)
								except:
									print "Oops! no se ha podido borrar."
						except:
							print"Oops! error al leer fichero."
					if "mp4" in name:
						encontrado = True
						print "uploading " + name
						src = root +"/"+ name
						dst = data["upload_dir"]+"/"+filemask["value"]+"/"+name
						try:
 							move( src, dst)
							if not os.path.isfile(src):
								try:
									print "Borrando........"
									#rmtree(root,ignore_errors=True)
								except:
									print "Oops! no se ha podido borrar."
						except:
							print"Oops! error al leer fichero."
					if not encontrado:
						try:
							print "Borrando........"
							#rmtree(root,ignore_errors=True)
						except:
							print "Oops! no se ha podido borrar."

	print "-------------------------------------------------------------"
	print "\n\n"

