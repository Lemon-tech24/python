array = [1, 2, 3, 4, 5]


def check(index):
    if index in array:
        array.index(index)
        return True
    return False


if check(3):
    print('in array')
else:
    print('not in array')