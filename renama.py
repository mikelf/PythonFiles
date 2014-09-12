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
	print filename
	if u"ññ" in filename:
		print "encontrado"
	#os.rename("Joe Blow", "Blow, Joe")


