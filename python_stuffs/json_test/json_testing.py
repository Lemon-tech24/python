import json

filename = './data.json'


def viewData():
    i = 0
    with open(filename, 'r') as f:
        temp = json.load(f)
        for entry in temp:
            say = entry['say']
            name = entry['name']
            print(f'index number: {i}')
            print(f'sayings: {say}')
            print(f'names: {name}')
            i += 1
def add_data():
    data = {}
    with open(filename, 'r') as f:
        temp = json.load(f)
    data["say"] = input('add say')
    data["name"] = input('add name')

    temp.append(data)
    with open(filename, 'w') as f:
        json.dump(temp, f, indent=3)


def deleteData():

    new_data = []
    with open(filename, "r") as f:
        temp = json.load(f)
        data_len = len(temp)-1
        option = input(f'select number you want to delete')
        i = 0

        for entry in temp:
            if i == int(option)-1:
                pass
                i += 1
            else:
                new_data.append(entry)
                i += 1
        with open(filename, 'w') as f:
            json.dump(new_data, f, indent=3)

