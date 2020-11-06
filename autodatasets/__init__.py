__version__ = "0.0.1"

from .data_reader import create_reader
from .data_downloader import download
from .utils import *

from . import object_detection
from . import image_classification

import logging
logging.basicConfig(format='[autodatasets:%(filename)s:L%(lineno)d] %(levelname)-6s %(message)s')
logging.getLogger().setLevel(logging.INFO)
