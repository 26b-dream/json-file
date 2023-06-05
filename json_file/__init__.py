"""Class for JSON files"""
from __future__ import annotations

import json
from typing import TYPE_CHECKING

from extended_path import ExtendedPath

if TYPE_CHECKING:
    import os
    from datetime import date, datetime
    from typing import Any


class JSONFile(ExtendedPath):
    """Class for JSON files"""

    def __init__(
        self,
        *_args: str | bytes | os.PathLike[str] | int | datetime | date | float,
    ) -> None:
        self.parsed_cached_value = None
        super().__init__()

    def parsed(self) -> Any:
        """Read and parse a JSON file

        Returns:
            Any: The parsed JSON"""

        # I don't know of any reason why you would want to use read_text instead of read_bytes for JSON. Unless a
        # specific need arises this function will always just use read_bytes
        return json.loads(self.read_bytes())

    def parsed_cached(self, reload: bool = False) -> Any:
        """Read a file, parse it using json.loads, then cache the result

        Args:
            reload (bool, optional): If True, reload the file into the cache. Defaults to False.

        Returns:
            Any: Parsed JSON file"""

        # I don't know of any reason why you would want to use read_text instead of read_bytes for JSON. Unless a
        # specific need arises this function will always just use read_bytes
        if not self.parsed_cached_value or reload:
            self.parsed_cached_value = json.loads(self.read_bytes_cached(reload))

        return self.parsed_cached_value
