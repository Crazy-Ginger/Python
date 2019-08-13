#!/usr/bin/env python3
from lxml import html
import requests

page = requests.get('https://www.timeanddate.com/sun/uk/huddersfield')
tree = html.fromstring(page.content)

# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# prices = tree.xpath('//span[@class="item-price"]/text()')

# print (page.text)
opFile = open("DateTime.html", "w")
opFile.write(page.text)
opFile.close()


#print ('buyers: ', buyers)
#print ('prices: ', prices)

