#-*- coding: utf-8 -*-
import json
import urllib.request
from json2html import json2html

url = "http://services.fmtc.co/v2/getDeals?key=fb6e3f91d9792a1c36740363feb0fd17"
json_data = urllib.request.urlopen(url)
json_data = open('C:\\Users\\user1\\Desktop\\dealsSingle.json')
parsed_json_data = json_data.read()
json_ready_decoded_data = '{{\"Data\":{}}}'.format(parsed_json_data) #'{{\"Data\":{}}}'.format(parsed_json_data.decode('utf-8'))
string_json_data = (json.loads(json_ready_decoded_data))


print(json_ready_decoded_data)
print(string_json_data)
print(json2html.convert(json = string_json_data))

json_data.close()