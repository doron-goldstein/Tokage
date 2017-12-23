"""Utilities for the library"""

import re
from .partial import PartialAnime, PartialCharacter, PartialManga, PartialPerson


def create_relation(kwargs):
    if kwargs.get('type') == "anime":
        return PartialAnime.from_related(kwargs)
    else:
        return PartialManga.from_related(kwargs)


def parse_id(link):
    """Get ID from a myanimelist link."""
    pattern = r'(?:\/([\d]+)\/)'
    match = re.search(pattern, link)
    if match:
        target_id = match.group(1)
        return target_id
    else:
        return None
