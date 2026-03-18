import os
from typing import Dict, List

class SearchFiles:
    def __init__(self, path: str):
        self.directory = os.fsencode(path)
        self._result_files: Dict[bytes, List[bytes]] = {}
        self.count = 0

    def add(self, dirpath: bytes, filename: bytes):
        catalog = dirpath.split(sep=b'/')[-1]
        self._result_files.setdefault(catalog, [])
        full_path = os.path.join(dirpath, filename)
        self._result_files[catalog].append(full_path)
        self.count += 1

    @property
    def data(self) -> Dict[bytes, List[bytes]]:
        return self._result_files

    def search(self, extension: bytes = b'.md'):
        for dirpath, dirnames, filenames in os.walk(self.directory):
            for filename in filenames:
                if filename.endswith(extension):
                    self.add(dirpath, filename)