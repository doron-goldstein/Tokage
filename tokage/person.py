"""Person object"""

from .partial import PartialAnime, PartialManga
from .utils import parse_id


class Person:
    """Represents a MAL Person (Voice Actors, Staff, etc.)

    Attributes
    ----------
    id : int
        The Person's ID.

    name : str
        The Person's name.

    link : str
        Link to the Person on MAL.

    image : str
        Image URL of the Person.

    favorites : int
        Amount of favorites the Person has.

    anime : list[:class:`PartialAnime`]
        Staff positions in Anime.

    manga : list[:class:`PartialManga`]
        Published Manga.

    more : str
        Additional info about the Person.

    website : str
        Link to the Person's website

    voice_acting : list[dict]
        WIP - List of characters the Person has voice acted.

    """

    def __init__(self, person_id, **kwargs):
        self.id = person_id
        self.link = kwargs.get('link_canonical')
        self.name = kwargs.get('name')
        self.image = kwargs.get('image_url')
        self.favorites = kwargs.get('member_favorites')
        self._raw_anime = kwargs.get('anime_staff_position')
        self._raw_manga = kwargs.get('published_manga')
        self.birthday = kwargs.get('birthday')
        self.more = kwargs.get('more')
        self.website = kwargs.get('website')
        self.voice_acting = kwargs.get('voice_acting_role')  # TODO: Handle

    @property
    def anime(self):
        lst = []
        for position in self._raw_anime:
            anime = position['anime']
            anime['mal_id'] = parse_id(anime['url'])
            anime['relation'] = position['role']
            anime['title'] = anime.pop('name')
            obj = PartialAnime.from_related(anime)
            lst.append(obj)
        return lst

    @property
    def manga(self):
        lst = []
        for position in self._raw_manga:
            manga = position['manga']
            manga['mal_id'] = parse_id(manga['url'])
            manga['relation'] = position['role']
            manga['title'] = manga.pop('name')
            obj = PartialManga.from_related(manga)
            lst.append(obj)
        return lst
