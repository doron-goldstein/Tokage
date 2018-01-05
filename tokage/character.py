"""Character object"""

from .utils import parse_id
from .partial import PartialAnime, PartialManga, PartialPerson


class Character:
    """Represents a MAL Character

    Attributes
    ----------
    id : int
        The Character's ID.

    name : str
        Character's name.

    link : str
        Link to the Character on MAL.

    image : str
        Image URL of the Character.

    favorites : int
        Amount of favorites the Character has.

    animeography : list[:class:`PartialAnime`]
        Anime the Character is featured in.

    mangaography : list[:class:`PartialManga`]
        Manga the Character is featured in.

    japanese_name : str
        Japanese name of the character.

    about : str
        WIP - Information about the character. As of now, spoilers are unformatted and will appear.

    voice_actors : list[:class:`PartialPerson`]
        List of voice actors who played this Character.

    """

    def __init__(self, char_id, **kwargs):
        self.id = char_id
        self.link = kwargs.get('link_canonical')
        self.name = kwargs.get('name')
        self.image = kwargs.get('image_url')
        self.favorites = kwargs.get('member_favorites')
        self._raw_animeography = kwargs.get('animeography')
        self._raw_mangaography = kwargs.get('mangaography')
        self.japanese_name = kwargs.get('name_kanji')
        self.about = kwargs.get('about')
        self._raw_voice_actors = kwargs.get('voice_actors') or kwargs.get('voice_actor')

    @property
    def animeography(self):
        lst = []
        for anime in self._raw_animeography:
            anime['id'] = parse_id(anime['url'])
            obj = PartialAnime.from_character(anime)
            lst.append(obj)
        return lst

    @property
    def mangaography(self):
        lst = []
        for manga in self._raw_mangaography:
            manga['id'] = parse_id(manga['url'])
            obj = PartialManga.from_character(manga)
            lst.append(obj)
        return lst

    @property
    def voice_actors(self):
        lst = []
        for va in self._raw_voice_actors:
            va['id'] = parse_id(va['url'])
            obj = PartialPerson.from_voice_acting(va)
            lst.append(obj)
        return lst
