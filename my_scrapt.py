from lxml import html
import requests
import json
import os


listsuscriptions = []
def loadsuscrp():
	global listsuscriptions
	json_data=open('suscript.json')
	listsuscriptions = json.load(json_data)

def savenovedades():
    global listsuscriptions
    f = open("suscript.json","w")
    simplejson = json
    simplejson.dump(listsuscriptions,f)
    f.close()


loadsuscrp()
urls = listsuscriptions['urls']
for suscript in urls:
    page = requests.get(suscript['value'])
    tree = html.fromstring(page.text)
    raw_html = tree.xpath(suscript['key'])
    last_cap = 'unknow'
    for item in raw_html:
        if item.text != None:
            if suscript['data']  in item.text_content():
	        last_cap = item.text_content()
    last = suscript['last']
    if last != last_cap:
	suscript['last']= last_cap
        suscript['new']= '1'
    else:
        suscript['new']= '0'
    print('The last cap. of ' + suscript['id'] + ' is : ________________________________________' + last_cap)
print('*****************************************************')
print('******************* NEW CONTENT *********************')
print('*****************************************************')
for suscript in urls:
    if suscript['new'] == '1':
        print(suscript['id']+' - '+suscript['last'])
savenovedades()
