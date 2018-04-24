"""Character object"""

import tokage
from tokage.partial import PartialAnime, PartialManga, PartialPerson
from tokage.utils import parse_id


class Character(tokage.TokageBase):
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

    def __init__(self, char_id, data, **kwargs):
        self.id = char_id
        self.link = data.get('link_canonical')
        self.name = data.get('name')
        self.image = data.get('image_url')
        self.favorites = data.get('member_favorites')
        self._raw_animeography = data.get('animeography')
        self._raw_mangaography = data.get('mangaography')
        self.japanese_name = data.get('name_kanji')
        self.about = data.get('about')
        self._raw_voice_actors = data.get('voice_actors') or data.get('voice_actor')
        super().__init__(state=kwargs.get("state"))
        print(self._state)

    @property
    def animeography(self):
        lst = []
        for anime in self._raw_animeography:
            anime['mal_id'] = parse_id(anime['url'])
            obj = PartialAnime.from_character(anime, state=self._state)
            lst.append(obj)
        return lst

    @property
    def mangaography(self):
        lst = []
        for manga in self._raw_mangaography:
            manga['mal_id'] = parse_id(manga['url'])
            obj = PartialManga.from_character(manga, state=self._state)
            lst.append(obj)
        return lst

    @property
    def voice_actors(self):
        lst = []
        for va in self._raw_voice_actors:
            va['mal_id'] = parse_id(va['url'])
            obj = PartialPerson.from_voice_acting(va, state=self._state)
            lst.append(obj)
        return lst
