from shutil import copyfile
from photoshop import Session
from os import mkdir


def num2str(num: int, length: int = 2):
    length = 1 if length < 1 else length
    return '0' * (length - len(str(num))) + str(num)


sizes = [(26, 44), (27, 51), (28, 45), (29, 41), (30, 44)]

for ch, pgnum in sizes:
    try:
        mkdir(num2str(ch, 3))
    except FileExistsError:
        pass

    for pg in range(1, pgnum, 5):
        expg = pg + 4 if pg + 4 <= pgnum else pgnum
        new_file_name = f'{num2str(ch, 3)}/Aot-{num2str(ch, 3)}-st({num2str(pg, 2)}-{num2str(expg, 2)}).psd'
        copyfile(f'template.psd', new_file_name)
        print(new_file_name, end=' - ')

        with Session(new_file_name, action="open") as ps:
            for i, num in enumerate(range(pg, expg+1)):
                ps.active_document.layers[i].name = num2str(num, 2)
                print('.', end='')
            ps.active_document.saveAs(
                new_file_name, ps.PhotoshopSaveOptions(), True)
            ps.active_document.close()

        print()
