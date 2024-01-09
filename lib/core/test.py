import os
import sys
import csv

sys.path.append(os.getcwd())

try:
    pass
except ImportError:
    import requests
finally:
    import requests

import requests

try:
    from lib.core.extractor import extract_the_mac
except ImportError:
    from extractor import extract_the_mac

import settings
from logger import logger


d = extract_the_mac()
for datas in d:
    req = requests.post("https://www.ipchecktool.com/tool/macfinder?oui=56%3A72%3A59%3AD5%3A3C%3A7B&page=1",data="F6:4E:40:70:C5:69")
    print("The specified MAC address or manufacturer was not found in the database." not in req.text)
    # if "The specified MAC address or manufacturer was not found in the database." not in req.text:
        # print(True)