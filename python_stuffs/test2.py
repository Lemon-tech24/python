import random

fName = ['Carl', 'John', 'Mark', 'John Paul', 'Paul', 'Ricardo', 'Brian', 'Max', 'Adrian']
lName = ['Marx', 'Dela cruz', 'Villanueva', 'Ong', 'Lee', 'Dela rosa', 'Dela santos', 'Santos', 'lopez']

for num in range(5):
    #first = random.choice(fName)
    #last = random.choice(lName)
    #print(first + " " + last)


    first = random.randint(0, len(fName))
    last = random.randint(0, len(lName))

    firstt = fName[first]
    lastt = lName[last]


    print(firstt +" "+ lastt)

