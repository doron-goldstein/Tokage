"""
Tokage is an async MAL wrapper for Python 3.5+.

.. currentmodule:: tokage

.. autosummary::
    :toctree: Tokage

    client
    anime
    manga
    character
    person
    errors
"""

# flake8: noqa

from .client import Client
from .errors import *
from .anime import Anime
from .manga import Manga
from .character import Character
from .person import Person
from .partial import PartialAnime, PartialManga, PartialCharacter, PartialPerson
