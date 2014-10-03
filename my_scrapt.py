from lxml import html
import requests
import json
import os


lissuscriptions = []
def loadsuscrp():
	global lissuscriptions
	json_data=open('suscript.json')
	lissuscriptions = json.load(json_data)

loadsuscrp()
urls = lissuscriptions['urls']
for suscript in urls:
    page = requests.get(suscript['value'])
    tree = html.fromstring(page.text)
    raw_html = tree.xpath(suscript['key'])
    last_cap = 'unknow'
    for item in raw_html:
        if item.text != None:
            if suscript['data']  in item.text_content():
	        last_cap = item.text_content()
    print('The last cap. of ' + suscript['id'] + ' is ' + last_cap)

