import json

json_file = open('data.json', 'r', encoding='utf-8')

data = json.load(json_file)

print(data['id'])