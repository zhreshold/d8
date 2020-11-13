# This file is generated from image_classification/constructing.md automatically through:
#    d2lbook build lib
# Don't edit it directly

from typing import Sequence, Dict, Union, Callable, Any, Optional
from d8.image_classification import Dataset

#@save_cell
from_folders_meta: Sequence[Dict[str, Union[Sequence[str], str]]] = [
    {'name' : 'ibeans',
     'url'  : [f'https://storage.googleapis.com/ibeans/{part}.zip' for part in ('train', 'validation', 'test')],
     'root' : '*'},
    {'name' : 'boat',
     'url'  : 'https://www.kaggle.com/clorichel/boat-types-recognition',
     'root' : '.'},
    {'name' : 'intel',
     'url'  : 'https://www.kaggle.com/puneet6060/intel-image-classification',
     'root' : ('*/seg_train', '*/seg_test')},
    {'name' : 'fruits-360',
     'url'  : 'https://www.kaggle.com/moltean/fruits',
     'root' : ('*/Training', '*/Test')},
    {'name' : 'caltech-256',
     'url'  : 'https://www.kaggle.com/jessicali9530/caltech256',
     'root' : '256_ObjectCategories'},
    {'name' : 'cub-200',
     'url'  : 'https://www.kaggle.com/tarunkr/caltech-birds-2011-dataset',
     'root' : '*/images'},
    {'name' : 'cifar10',
     'url'  : 'https://www.kaggle.com/swaroopkml/cifar10-pngs-in-folders',
     'root' : ('*/train', '*/test')},
    {'name' : 'citrus-leaves',
     'url'  : 'https://www.kaggle.com/dtrilsbeek/citrus-leaves-prepared',
     'root' : ('*/train', '*/validation')},
    {'name' : 'cmaterdb',
     'url'  : 'https://www.kaggle.com/ipythonx/ekush-bangla-handwritten-data-numerals',
     'root' : '.'},
    {'name' : 'cassava',
     'url'  : 'https://www.kaggle.com/cassava-disease:train.zip',
     'root' : 'train'},
    {'name' : 'dtd',
     'url'  : 'https://www.kaggle.com/jmexpert/describable-textures-dataset-dtd',
     'root' : 'dtd/images'},
    {'name' : 'eurosat',
     'url'  : 'https://www.kaggle.com/apollo2506/eurosat-dataset',
     'root' : 'EuroSAT'},
    {'name' : 'food-101',
     'url'  : 'https://www.kaggle.com/kmader/food41',
     'root' : 'images'},
    {'name' : 'horses-or-humans',
     'url'  : 'https://www.kaggle.com/sanikamal/horses-or-humans-dataset',
     'root' : ('*/train', '*/validation')},
    {'name' : 'malaria',
     'url'  : 'https://www.kaggle.com/iarunava/cell-images-for-detecting-malaria',
     'root' : 'cell_images'},
    {'name' : 'flower-102',
     'url'  : 'https://www.kaggle.com/lenine/flower-102diffspecies-dataset',
     'root' : ('*/train', '*/valid')},
    {'name' : 'green-finder',
     'url'  : 'https://www.kaggle.com/tobiek/green-finder',
     'root' : '*'},
    {'name' : 'leaves',
     'url'  : 'https://www.kaggle.com/rohit9086/leaves',
     'root' : ('*/train', '*/test')},
    {'name' : 'plant-village',
     'url'  : 'https://www.kaggle.com/abdallahalidev/plantvillage-dataset',
     'root' : '*/segmented'},
    {'name' : 'rock-paper-scissors',
     'url'  : 'https://www.kaggle.com/drgfreeman/rockpaperscissors',
     'root' : '.'},
    {'name' : 'sun-397',
     'url'  : 'https://www.kaggle.com/lash45/sun397-50-50',
     'root' : ('*/train', '*/test')},
    {'name' : 'chessman',
     'url'  : 'https://www.kaggle.com/niteshfre/chessman-image-dataset',
     'root' : '*/Chess'},
    {'name' : 'casting-products',
     'url'  : 'https://www.kaggle.com/ravirajsinh45/real-life-industrial-dataset-of-casting-product',
     'root' : '*'},
    {'name' : 'monkey-10',
     'url'  : 'https://www.kaggle.com/slothkong/10-monkey-species',
     'root' : '*'},
    {'name' : 'dog-cat-panda',
     'url'  : 'https://www.kaggle.com/ashishsaxena2209/animal-image-datasetdog-cat-and-panda',
     'root' : 'animals'},
    {'name' : 'broad-leaved-dock',
     'url'  : 'https://www.kaggle.com/gavinarmstrong/open-sprayer-images',
     'root' : '*'},
    {'name' : 'food-or-not-food',
     'url'  : 'https://www.kaggle.com/trolukovich/food5k-image-dataset',
     'root' : '*'},
    {'name' : 'gemstones',
     'url'  : 'https://www.kaggle.com/lsind18/gemstones-images',
     'root' : '*'},
    {'name' : 'hurricane-damage',
     'url'  : 'https://www.kaggle.com/kmader/satellite-images-of-hurricane-damage',
     'root' : ('train_another', 'validation_another')},
    {'name' : 'animal-10',
     'url'  : 'https://www.kaggle.com/alessiocorrado99/animals10',
     'root' : 'raw-img'},
    {'name' : 'walk-or-run',
     'url'  : 'https://www.kaggle.com/huan9huan/walk-or-run',
     'root' : '*'},
    {'name' : 'gender',
     'url'  : 'https://www.kaggle.com/cashutosh/gender-classification-dataset',
     'root' : '*'},
    {'name' : 'brain-tumor',
     'url'  : 'https://www.kaggle.com/simeondee/brain-tumor-images-dataset',
     'root' : '*'},
    {'name' : 'facial-expression',
     'url'  : 'https://www.kaggle.com/astraszab/facial-expression-dataset-image-folders-fer2013',
     'root' : '*'},
    {'name' : 'rice-diseases',
     'url'  : 'https://www.kaggle.com/minhhuy2810/rice-diseases-image-dataset',
     'root' : '*'},
    {'name' : 'mushrooms',
     'url'  : 'https://www.kaggle.com/maysee/mushrooms-classification-common-genuss-images',
     'root' : '*'},
    {'name' : 'oregon-wildlife',
     'url'  : 'https://www.kaggle.com/virtualdvid/oregon-wildlife',
     'root' : '*'},
    {'name' : 'bird-225',
     'url'  : 'https://www.kaggle.com/gpiosenka/100-bird-species',
     'root' : '*'},
]

for x in from_folders_meta:
    Dataset.add(x['name'], Dataset.from_folders, (x['url'], x['root']))

#@save_cell
from_label_func_meta: Sequence[Dict[str, Union[Callable[[Any], Optional[str]], Sequence[str], str]]] = [
    {'name' : 'stanford-dogs',
     'url'  : 'https://www.kaggle.com/jessicali9530/stanford-dogs-dataset',
     'func' : lambda path: path.parent.name.split('-')[1].lower()},
    {'name' : 'butterfly',
     'url'  : 'https://www.kaggle.com/veeralakrishna/butterfly-dataset',
     'func' : lambda path: path.stem[:3] if 'images' in str(path) else None},
    {'name' : 'cub-200',
     'url'  : 'https://www.kaggle.com/tarunkr/caltech-birds-2011-dataset',
     'func' : lambda path: path.parent.name.split('.')[1].lower() if 'images' in str(path) else None},
    {'name' : 'dogs-vs-cats',
     'url'  : 'https://www.kaggle.com/dogs-vs-cats:train.zip',
     'func' : lambda path: path.name.split('.')[0]},
    {'name' : 'deep-weeds',
     'url'  : 'https://www.kaggle.com/coreylammie/deepweedsx',
     'func' : lambda path: path.with_suffix('').name.split('-')[-1]},
    {'name' : 'oxford-pets',
     'url'  : 'https://www.kaggle.com/alexisbcook/oxford-pets',
     'func' : lambda path: path.name.split('_')[0].lower() if 'images' in str(path) else None},
    {'name' : 'lego-brick',
     'url'  : 'https://www.kaggle.com/joosthazelzet/lego-brick-images',
     'func' : lambda path: path.name.split(' ')[0].lower() if str(path).startswith('dataset') else None},
    {'name' : 'satelite-plane',
     'url'  : 'https://www.kaggle.com/rhammell/planesnet',
     'func' : lambda path: path.name.split('__')[0]},
    {'name' : 'honey-bee',
     'url'  : 'https://www.kaggle.com/jenny18/honey-bee-annotated-images',
     'func' : lambda path: path.name.split('_')[0]},
    {'name' : 'coil-100',
     'url'  : 'https://www.kaggle.com/jessicali9530/coil100',
     'func' : lambda path: path.name.split('__')[0]},
    {'name' : 'flower-10',
     'url'  : 'https://www.kaggle.com/aksha05/flower-image-dataset',
     'func' : lambda path: path.name.split('_')[0].lower()}
]

for y in from_label_func_meta:
    Dataset.add(y['name'], Dataset.from_label_func, (y['url'], y['func']))

