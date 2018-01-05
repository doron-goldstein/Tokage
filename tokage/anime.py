"""Anime object"""

from .utils import create_relation


class Anime:
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

    def __init__(self, anime_id, **kwargs):
        self.id = anime_id
        self.title = kwargs.get('title')
        self.type = kwargs.get('type')
        self.synonyms = kwargs.get('title_synonyms')
        self.image = kwargs.get('image_url')
        self.japanese_title = kwargs.get('title_japanese')
        self.status = kwargs.get('status')
        self.episodes = kwargs.get('episodes')
        self.airing = kwargs.get('airing')

        self._air_time = kwargs.get('aired_string')
        if " to " not in self._air_time:
            self.air_start = self._air_time
            self.air_end = None
        else:
            self.air_start, self.air_end = self._air_time.split(" to ")

        self.premiered = kwargs.get('premiered')
        self.broadcast = kwargs.get('broadcast')
        self.synopsis = kwargs.get('synopsis')
        self.producers = kwargs.get('producer')
        self.licensors = kwargs.get('licensor')
        self.studios = kwargs.get('studio')
        self.source = kwargs.get('source')
        self._raw_genres = kwargs.get('genre') or kwargs.get('genres')
        self.duration = kwargs.get('duration')
        self.link = kwargs.get('link_canonical')
        self.rating = kwargs.get('rating')
        self.score = kwargs.get('score')
        self.rank = kwargs.get('rank')
        self.popularity = kwargs.get('popularity')
        self.members = kwargs.get('members')
        self.favorites = kwargs.get('favorites')
        self._raw_related = kwargs.get('related')

    @property
    def genres(self):
        return [g['name'] for g in self._raw_genres] if self._raw_genres else None

    @property
    def related(self):
        lst = []
        for relation_type, relations in self._raw_related.items():
            for relation in relations:
                relation['relation'] = relation_type
                obj = create_relation(relation)
                lst.append(obj)
        return lst
