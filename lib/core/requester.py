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

class Requester:
    def __init__(self) -> None:
        self._extractor = extract_the_mac()
        self._macsaddrr = [line for line in self._extractor]
        self.url = "https://www.ipchecktool.com/tool/macfinder?oui=56%3A72%3A59%3AD5%3A3C%3A7B&page=1"
        self._request = None
        self.failed_response = "The specified MAC address or manufacturer was not found in the database."
        self._valids = []

    def _validate_requests_for_mac_address(self, value):
        try:
            logger.info("starting")
            valid_macs = []

            for _macadrr in value:
                self._request = requests.post(self.url, data= _macadrr)
                logger.info("testing %s" % _macadrr)
                if not self.failed_response in self._request.text:
                    settings.FOUND_MAC = True
                    logger.info("got the target")
                    valid_macs.append(_macadrr)

            return valid_macs

        except requests.exceptions.RequestException as ex:
            logger.error(ex)

    def get_macs(self):
        valid_macs = self._validate_requests_for_mac_address(self._macsaddrr)

        # Write valid MAC addresses to a CSV file
        csv_file_path = "valid_mac.csv"
        with open(csv_file_path, mode='w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Valid MAC Addresses'])  # Write header

            for mac in valid_macs:
                csv_writer.writerow([mac])

        return valid_macs

obj = Requester()
req = obj.get_macs()
print(req)
