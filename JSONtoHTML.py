import json
from json2html import json2html


json_data = open('I:\\jsontest.json')
parsed_json_data = json_data.read()
string_json_data = json.loads(parsed_json_data)


print(string_json_data)
print(json2html.convert(json = string_json_data))


json_data.close()