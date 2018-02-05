"""Utilities for the library"""

import re
from tokage.partial import PartialAnime, PartialManga


def create_relation(data, state):
    if data.get('type') == "anime":
        return PartialAnime.from_related(data, state=state)
    else:
        return PartialManga.from_related(data, state=state)


def parse_id(link):
    """Get ID from a myanimelist link."""
    pattern = r'(?:\/([\d]+)\/)'
    match = re.search(pattern, link)
    if match:
        target_id = match.group(1)
        return target_id
    else:
        return None
