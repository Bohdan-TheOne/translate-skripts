from os import rename


def num2str(num: int, length: int = 2):
    length = 1 if length < 1 else length
    return '0' * (length - len(str(num))) + str(num)

ch = '014'
st = 3
fn = 54

for i in range(st - 1, fn):
    rename(f'{ch}-{num2str(i + 1)}.jpg', f'{ch}-{num2str(i)}.jpg')
