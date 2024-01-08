import os
import sys
sys.path.append(os.getcwd())
import thirdparty.requests as requests 
from lib.core.extractor import extractthe_mac


class Requester:
    def __init__(self) -> None:
        self._extractor = extractthe_mac()
        self.url = "https://www.ipchecktool.com/tool/macfinder?oui=56%3A72%3A59%3AD5%3A3C%3A7B&page=1"
        self._request = None
        self.failed_response = "The specified MAC address or manufacturer was not found in the database."
    def _validate_requests_for_mac_address(self):
        for _macadrr in self._extractor:
            self._request = requests.get(self.url,params=_macadrr)
            if not self.failed_response in self._request:
                return True
            return False
        
    def get_macs(self):
        return self._validate_requests_for_mac_address()

obj = Requester()
obj.get_macs()
