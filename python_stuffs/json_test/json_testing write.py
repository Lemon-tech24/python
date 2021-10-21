import json

filename = 'data.json'

with open(filename, 'r') as f:
    data = {}

    i = 0
    read_content = json.load(f)

    while i < len(read_content):
        i = i + 1

    data['id'] = i
    read_content.append(data)
    with open(filename, 'w') as a:
        json.dump(read_content, a , indent=3)

