"""Anime object"""

import tokage
from tokage.utils import create_relation


class Anime(tokage.TokageBase):
    """Represents a MAL Anime

    Attributes
    ----------
    id : int
        The Anime's ID.

    title : str
        The Series title.

    type : str
       The Anime's type. Can be `ONA`/`OVA`/`TV`/`Movie`.

    synonyms : list[str]
       Alternative names for the Anime.

    image : str
        The cover image URL for the Anime.

    japanese_title : str
        Japanese title of the Anime.

    status : str
        Airing status of the Manga.

    episodes : int
        Episode count of the Manga.

    air_start : str
        Airing start date.

    air_end : str
        Airing end date.

    airing : bool
        True if the Anime is airing, False if not.

    synopsis : str
        Description of the Anime.

    producers : list[list]
        WIP - List of the Anime's producers.

    licensors : list[list]
        WIP - List of the Anime's licensors.

    studios : list[list]
        WIP - List of the Anime's studios

    premiered : str
        Premier season.

    broadcast : str
        Broadcast times.

    genres : list[str]
        List of the Anime's genres.

    link : str
        Link to the Anime on MAL.

    score : tuple(int)
        Tuple of (score, voters).

    duration : str
        Duration of the Anime (may be per episode).

    rank : int
        Anime's rank on the MAL board.

    popularity : int
        Popularity rank of the Anime.

    members : int
        Amount of members which have the Anime in their list.

    favorites : int
        Amount of favorites given to the Anime.

    source : str
        Type of source material. Can be `Manga` `Novel` or `Original`.

    related : list[:class:`.PartialAnime` or :class:`.PartialManga`]
        List of related Anime or Manga.

    """

    def __init__(self, anime_id, data, **kwargs):
        self.id = anime_id
        self.title = data.get('title')
        self.type = data.get('type')
        self.synonyms = data.get('title_synonyms')
        self.image = data.get('image_url')
        self.japanese_title = data.get('title_japanese')
        self.status = data.get('status')
        self.episodes = data.get('episodes')
        self.airing = data.get('airing')

        self._air_time = data.get('aired_string')
        if " to " not in self._air_time:
            self.air_start = self._air_time
            self.air_end = None
        else:
            self.air_start, self.air_end = self._air_time.split(" to ")

        self.premiered = data.get('premiered')
        self.broadcast = data.get('broadcast')
        self.synopsis = data.get('synopsis')
        self.producers = data.get('producer')
        self.licensors = data.get('licensor')
        self.studios = data.get('studio')
        self.source = data.get('source')
        self._raw_genres = data.get('genre') or data.get('genres')
        self.duration = data.get('duration')
        self.link = data.get('link_canonical')
        self.rating = data.get('rating')
        self.score = data.get('score')
        self.rank = data.get('rank')
        self.popularity = data.get('popularity')
        self.members = data.get('members')
        self.favorites = data.get('favorites')
        self._raw_related = data.get('related')
        super().__init__(state=kwargs.get("state"))

    @property
    def genres(self):
        return [g['name'] for g in self._raw_genres] if self._raw_genres else None

    @property
    def related(self):
        lst = []
        for relation_type, relations in self._raw_related.items():
            for relation in relations:
                relation['relation'] = relation_type
                obj = create_relation(relation, self._state)
                lst.append(obj)
        return lst
