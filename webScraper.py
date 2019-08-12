#!/usr/bin/env python3
from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

buyers = tree.xpath('//div[@title="buyer-name"]/text()')
prices = tree.xpath('//span[@class="item-price"]/text()')

# print (page.content)

for char in page.content:
    if char == ">":
        print (char, "\n")
    else:
        print (char)


#print ('buyers: ', buyers)
#print ('prices: ', prices)

