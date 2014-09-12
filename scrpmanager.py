import json
import os
import sys

lissuscriptions = []

def loadsuscrp():
	global lissuscriptions
	json_data=open('data.json')
	lissuscriptions = json.load(json_data)

def printsuscrp():
    global lissuscriptions
    pos = 0
    folders = lissuscriptions["folder"]
    for cont in folders:
        mystr = "%s \t %s \t %s \t %s \t %s" % (str(pos), cont["id"], cont["res"], cont["last"], cont["value"])
        print(mystr)
        pos = pos+1

loadsuscrp()
if len(sys.argv) == 2:
    if sys.argv[1] == "show":
        printsuscrp()
else:
	print("Use scrpmanager + command")