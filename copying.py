from shutil import copyfile
from os import mkdir


def num2str(num: int, length: int = 2):
    length = 1 if length < 1 else length
    return '0' * (length - len(str(num))) + str(num)


ch = 30
pgnum = 45

try:
    mkdir(num2str(ch, 3))
except FileExistsError:
    pass

for pg in range(1, pgnum, 5):
    expg = pg + 4 if pg + 4 <= pgnum else pgnum
    copyfile(f'template.psd',
             f'{num2str(ch, 3)}/Aot-{num2str(ch, 3)}-st({num2str(pg, 2)}-{num2str(expg, 2)}).psd', )
