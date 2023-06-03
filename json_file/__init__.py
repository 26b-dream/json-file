from __future__ import annotations

import json
from typing import Any

from extended_path import ExtendedPath


class JSONFile(ExtendedPath):
    def parsed(self) -> Any:
        """Read and parse a JSON file"""

        # I don't know of any reason why you would want to use read_text instead of read_bytes for JSON
        # For now this function will always just use read_bytes
        return json.loads(self.read_bytes())

    def parsed_cached(self, reload: bool = False) -> Any:
        """Read and parse a JSON file with caching"""

        # I don't know of any reason why you would want to use read_text instead of read_bytes for BeautifulSoup
        # For now this function will always just use read_bytes
        if not hasattr(self, "parsed_cached_value") or reload:
            self.parsed_cached_value = json.loads(self.read_bytes_cached(reload))

        return self.parsed_cached_value
