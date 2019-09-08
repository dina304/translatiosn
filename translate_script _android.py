import csv
import json
from collections import OrderedDict

			
			
			
def replace_values(json,translate_dict):
	for key,val in json.items():
		if type(val) == OrderedDict:
			replace_values(val,translate_dict)
		else:
			if json[key].lower().encode('utf-8') in translate_dict.keys():
				json[key] = translate_dict[json[key].lower().encode('utf-8')].decode('utf-8')
			
			
bad_keys = []
not_found_keys = []
#creating dict of key and value
with open("data.csv") as csv_file:
	csv_reader = csv.DictReader(csv_file)
	translate_dict = {}
	for row in csv_reader:
		if row['KV NL Value'] != '' and row['KV BEFR Value'] != '' :
			translate_dict[row['KV NL Value'].lower()] = row['KV BEFR Value']

			
json_file = open("remote_strings_nlkruidvat.json", "rb+")
data = json_file.read()
json_dict = json.loads(data,object_pairs_hook=OrderedDict)
json_file.close()


replace_values(json_dict,translate_dict)


			


json_file = open("remote_strings_frkruidvat.json", "wb+")
json_file.write(json.dumps(json_dict))
json_file.close()
