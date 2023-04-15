import json
import yaml

with open("myfile.json","r") as json_file:
	ourjson = json.load(json_file)

print("El token de marcelo hidalgo  es: {}".format(ourjson['access_token']))
print("El token de marcelo hidalgo expira en: {} second.".format(ourjson['expires_in']))
