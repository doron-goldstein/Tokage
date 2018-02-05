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

from tokage.base import TokageBase
from tokage.client import Client
from tokage.errors import *
from tokage.anime import Anime
from tokage.manga import Manga
from tokage.character import Character
from tokage.person import Person
from tokage.partial import PartialAnime, PartialManga, PartialCharacter, PartialPerson
