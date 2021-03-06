# Reading Data

```eval_rst

.. currentmodule:: d8.core

```

We can use the :func:`create_reader` function to read data from various data format.

```eval_rst

.. autofunction:: create_reader

```

The `data_path` argument can be either a local folder path, a zip/tar file path, or a list of them. A more convenient way is passing a URL, or list of URL, that :func:`download` supports. For example, the following code download the Titanic competition data from Kaggle and list all files.

```{.python .input}
import pandas as pd

from d8 import core

reader = core.create_reader('https://www.kaggle.com/c/titanic', name='titanic')
reader.list_files()
```

Later on, we can open a file to read contents.

```{.python .input}
pd.read_csv(reader.open('train.csv')).head()
```

:func:`create_reader` returns an instance of :class:`Reader`. It provides methods to list and read files.

```eval_rst

.. autoclass:: Reader
   :members:
   :show-inheritance:
   :inherited-members:

```


```{.python .input  n=2}
#@save_all
#@hide_all
import abc
import glob
import io
import logging
import mimetypes
import os
import pathlib
import tarfile
import zipfile
from typing import List, Optional, Sequence, TypeVar, Union

import pandas as pd
import PIL
from PIL import ImageFile

from d8 import core

ImageFile.LOAD_TRUNCATED_IMAGES = True


__all__ = ['Reader', 'EmptyReader', 'FolderReader', 'TarReader', 'ZipReader', 'create_reader', 'listify']
```

```{.python .input}
#_E = TypeVar("_E")
#def listify(x: Optional[Union[_E, Sequence[_E]]]) -> List[_E]:
def listify(x):
    """Make x a list if it isn't."""
    return [] if not x else (list(x) if isinstance(x, (tuple, list)) else [x])
```

```{.python .input  n=3}
class Reader(abc.ABC):
    """The base class of the data reader.

    :param root: The root path.
    """
    def __init__(self, root: pathlib.Path):
        root = pathlib.Path(root)
        if not root.exists():
            raise NameError(f'{root} doesn\'t exists')
        self._root = root

    def __eq__(self, other) -> bool:
        if not isinstance(other, Reader):
            raise NotImplementedError()

        return self._root == other._root

    def __ne__(self, obj):
        return not self == obj

    @abc.abstractclassmethod
    def open(self, path: Union[str, pathlib.Path]):
        """Open file and return a stream.

        :param path: The relative file_path to the root
        :return: A file object depends on the reader type.
        """
        pass

    @abc.abstractclassmethod
    def _list_all(self) -> List[pathlib.Path]:
        pass

    def list_files(self, extensions: Sequence[str] =[], subfolders: Sequence[str] = []) -> List[pathlib.Path]:
        """List all files.

        :param extensions: If specified, then only keep files with extensions in this list.
        :return: The list of file paths.
        """
        # remove folders
        files = self._list_all()
        if extensions:
            files = [f for f in files if f.suffix.lower() in set(extensions)]
        if subfolders:
            files = [f for f in files if any([str(f).startswith(s) for s in subfolders])]
        return files

    def list_images(self, subfolders: Sequence[str] = []) -> List[pathlib.Path]:
        """List all image files.

        :return: The list of image file paths.
        """
        image_extensions = list(set(k for k,v in mimetypes.types_map.items() if v.startswith('image/')))
        return self.list_files(image_extensions, subfolders)

    def read_image(self, file_path: Union[str, pathlib.Path],
                   max_width: Optional[int] = None,
                   max_height: Optional[int] = None):
        """Read an image.

        :param file_path: The image file_path.
        :param max_width: The maximal width in pixel for the returned image.
            Specifying it with a small value may accelerate the reading.
        :param max_height: The maximal height in pixel for the returned image.
            Specifying it with a small value may accelerate the reading.
        :return: The image as a numpy array.
        """
        img = PIL.Image.open(self.open(file_path))
        if img.mode != 'RGB': img = img.convert('RGB')
        ratio = 0
        if max_width: ratio = max(ratio, img.size[0] / max_width)
        if max_height: ratio = max(ratio, img.size[1] / max_height)
        if ratio > 0:
            # TODO(mli) handle gray images
            img.draft('RGB',(int(img.size[0]/ratio), int(img.size[1]/ratio)))
        return img

    def get_image_info(self, image_paths: Sequence[str]) -> pd.DataFrame:
        """Query image information such as size, width and height.

        :param reader: The data reader.
        :param image_paths: The image file_paths to query.
        :return: The results with each image in a row.
        """
        rows = []
        for img_path in image_paths:
            raw = self.open(img_path).read()
            img = PIL.Image.open(io.BytesIO(raw))
            rows.append({'file_path':img_path, 'size (KB)':len(raw)/2**10,
                        'width':img.size[0], 'height':img.size[1]})
        return pd.DataFrame(rows)

```

```{.python .input}
class EmptyReader(Reader):
    def __init__(self):
        pass
    def _list_all(self):
        return []
    def open(self, path: Union[str, pathlib.Path]):
        raise ValueError('Empty reader cannot open a path')
    def __eq__(self, other) -> bool:
        if not isinstance(other, EmptyReader):
            raise NotImplementedError()
        return True

class FolderReader(Reader):
    def __init__(self, root: pathlib.Path):
        super().__init__(root)

    def open(self, path: Union[str, pathlib.Path]):
        return (self._root/path).open('rb')

    def _list_all(self):
        return [p.relative_to(self._root) for p in self._root.glob('**/*') if not p.is_dir()]

# Note that zip reader doesn't support multiprocess https://bugs.python.org/issue39363
class ZipReader(Reader):
    """A data reader to read from a zip file.

    :param root: The root path.
    """
    def __init__(self, root: pathlib.Path):
        super().__init__(root)
        self._root_fp = zipfile.ZipFile(self._root, 'r')

    def open(self, path: Union[str, pathlib.Path]):
        return self._root_fp.open(str(path))

    def _list_all(self):
        filenames = [file.filename for file in self._root_fp.infolist()
                     if not '__MACOSX' in file.filename and not file.is_dir()]
        return [pathlib.Path(fn) for fn in filenames]

class TarReader(Reader):
    """A data reader to read from a tar file.

    :param root: The root path.
    """
    def __init__(self, root: pathlib.Path):
        super().__init__(root)
        self._root_fp = tarfile.open(self._root, 'r')

    def open(self, path: Union[str, pathlib.Path]):
        return self._root_fp.open(str(path))

    def _list_all(self):
        return [pathlib.Path(fn) for fn in self._root_fp.getmembers()]
```

```{.python .input}
def create_reader(data_path: Union[str, Sequence[str]],
                  name : Optional[str] = None) -> Reader:
    """Create a data reader.

    :param data_path: Either local or remote.
    :return: The created data reader
    """
    paths = listify(data_path)
    local_paths = [(pathlib.Path(p) if pathlib.Path(p).exists() else core.download(
        str(p), name, extract=True)) for p in paths]
    local_paths = list(set(local_paths))
    if len(local_paths) == 0:
        return EmptyReader()
    if len(local_paths) > 1:
        raise NotImplementedError()
    path = local_paths[0]
    if path.is_dir():
        return FolderReader(path)
    if path.suffix == '.zip':
        return ZipReader(path)
    if path.suffix in ['.tar', '.tgz', '.gz']:
        return TarReader(path)
    raise ValueError(f'Not support {path}')
```

```{.python .input}
import unittest

class TestListify(unittest.TestCase):
    def test_listify(self):
        self.assertEqual(listify(None), [])
        self.assertEqual(listify(1), [1,])
        self.assertEqual(listify([1,2,3]), [1,2,3])
        self.assertEqual(listify(('a',1,)), ['a',1])

class TestReader(unittest.TestCase):
    def test_create_reader(self):
        name = 'test_reader'
        for fn in (core.DATAROOT/name).glob('*'): fn.unlink()

        r = create_reader('https://www.kaggle.com/c/titanic', name)
        self.assertEqual(type(r), FolderReader)
        self.assertEqual(sorted(r.list_files(['.zip', '.csv'])),
                         sorted([pathlib.Path('test.csv'), pathlib.Path('titanic.zip'), pathlib.Path('train.csv'), pathlib.Path('gender_submission.csv')]))

        r = create_reader('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', name)
        with r.open('iris.data') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 151)

    def test_equal(self):
        a = create_reader('/')
        b = create_reader('/')
        self.assertEqual(a, b)
```

```{.python .input}
%load_ext mypy_ipython
%mypy

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
```
