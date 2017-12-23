"""Character object"""

from .utils import parse_id
from .partial import PartialAnime, PartialManga


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

    voice_actors : list[dict]
        WIP - List of voice actors who played this Character.

    """

    def __init__(self, char_id, **kwargs):
        self.id = char_id
        self.link = kwargs.pop('link_canonical', None)
        self.name = kwargs.pop('name', None)
        self.image = kwargs.pop('image_url', None)
        self.favorites = kwargs.pop('member_favorites', None)

        self.animeography = []
        self._raw_animeography = kwargs.pop('animeography', None)
        for anime in self._raw_animeography:
            anime['id'] = parse_id(anime['url'])
            obj = PartialAnime.from_character(anime)
            self.animeography.append(obj)

        self.mangaography = []
        self._raw_mangaography = kwargs.pop('mangaography', None)
        for manga in self._raw_mangaography:
            manga['id'] = parse_id(manga['url'])
            obj = PartialManga.from_character(manga)
            self.mangaography.append(obj)

        self.japanese_name = kwargs.pop('name_kanji', None)
        self.about = kwargs.pop('about', None)
        self.voice_actors = kwargs.pop('voice_actors', None)  # TODO: Handle
