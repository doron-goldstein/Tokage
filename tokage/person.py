"""Person object"""

import tokage
from tokage.partial import PartialAnime, PartialCharacter, PartialManga
from tokage.utils import parse_id


class Person(tokage.TokageBase):
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

    voice_acting : list[:class:`PartialCharacter`]
        List of characters the Person has voice acted.

    """

    def __init__(self, person_id, data, **kwargs):
        self.id = person_id
        self.link = data.get('link_canonical')
        self.name = data.get('name')
        self.image = data.get('image_url')
        self.favorites = data.get('member_favorites')
        self.birthday = data.get('birthday')
        self.more = data.get('more')
        self.website = data.get('website')
        self._raw_anime = data.get('anime_staff_position')
        self._raw_manga = data.get('published_manga')
        self._raw_voice_acting = data.get('voice_acting_role')
        super().__init__(state=kwargs.get("state"))

    @property
    def voice_acting(self):
        lst = []
        for va in self._raw_voice_acting:
            char = va['character']
            char['mal_id'] = parse_id(char['url'])
            anime = va['anime']
            anime['mal_id'] = parse_id(anime['url'])
            anime_obj = PartialAnime.from_character(anime, state=self._state)
            obj = PartialCharacter.from_person(char, anime_obj, state=self._state)
            lst.append(obj)
        return lst

    @property
    def anime(self):
        lst = []
        for position in self._raw_anime:
            anime = position['anime']
            anime['mal_id'] = parse_id(anime['url'])
            anime['relation'] = position['role']
            anime['title'] = anime.pop('name')
            obj = PartialAnime.from_related(anime, state=self._state)
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
            obj = PartialManga.from_related(manga, state=self._state)
            lst.append(obj)
        return lst
