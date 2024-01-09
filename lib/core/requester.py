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
        self.url = url = "https://api.macvendors.com/%s"
        self._request = None
        self.failed_response = "The MAC address does not belong to any registered block."
        self.succed = "has been assigned by the"
        self._valids = []

    def _validate_requests_for_mac_address(self):
        try:
            logger.info("starting")
            valid_macs = []

            for _macadrr in self._extractor:
                self._request = requests.get(self.url%_macadrr)
                logger.debug("testing %s" % _macadrr)
                if self._request.status_code == 200:
                    logger.info("mac address: %s is valid!!!"%_macadrr)
                    settings.FOUND_MAC = True
                    logger.info("macaddress is valid")
                    valid_macs.append(_macadrr)

            return valid_macs

        except requests.exceptions.RequestException as ex:
            logger.error(ex)

    def get_macs(self):
        pass

obj = Requester()
req = obj._validate_requests_for_mac_address()
print(req)
