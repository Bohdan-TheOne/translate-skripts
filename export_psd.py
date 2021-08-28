from psd_tools import PSDImage
from os import listdir, mkdir

name = 'Aot-024'

docs = [i for i in listdir() if i.endswith('.psd')]
print(docs)

try:
    mkdir(name)
except FileExistsError:
    pass

for doc in docs:
    psd = PSDImage.open(doc)

    for i, _ in enumerate(psd):
        psd[i].visible = True
        print(psd[i])
        layer_image = psd[i].composite(force=True)
        layer_image.save(f'{name}/{psd[i].name}.png')
