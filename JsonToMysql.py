import json
import urllib.request


url = "http://services.fmtc.co/v2/getDeals?key=fb6e3f91d9792a1c36740363feb0fd17"
response = urllib.request.urlopen(url)
parsed_response = response.read()
decoded_parsed_response = parsed_response.decode('utf-8')
json_data = json.loads(decoded_parsed_response)

print(response)
print(parsed_response)
print(decoded_parsed_response)
print(json_data)
