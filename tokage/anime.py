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
        self.title = kwargs.pop('title', None)
        self.type = kwargs.pop('type', None)
        self.synonyms = kwargs.pop('title_synonyms', None)
        self.image = kwargs.pop('image_url', None)
        self.japanese_title = kwargs.pop('title_japanese', None)
        self.status = kwargs.pop('status', None)
        self.episodes = kwargs.pop('episodes', None)
        self.airing = kwargs.pop('airing', None)

        self._air_time = kwargs.pop('aired_string', None)
        if " to " not in self._air_time:
            self.air_start = self._air_time
            self.air_end = None
        else:
            self.air_start, self.air_end = self._air_time.split(" to ")

        self.premiered = kwargs.pop('premiered', None)
        self.broadcast = kwargs.pop('broadcast', None)
        self.synopsis = kwargs.pop('synopsis', None)
        self.producers = kwargs.pop('producer', None)
        self.licensors = kwargs.pop('licensor', None)
        self.studios = kwargs.pop('studio', None)
        self.source = kwargs.pop('source', None)

        self._raw_genres = kwargs.pop('genre', None)
        if self._raw_genres is None:
            self._raw_genres = kwargs.pop('genres', None)
        self.genres = [g['name'] for g in self._raw_genres] if self._raw_genres else None

        self.duration = kwargs.pop('duration', None)
        self.link = kwargs.pop('link_canonical', None)
        self.rating = kwargs.pop('rating', None)
        self.score = kwargs.pop('score', None)
        self.rank = kwargs.pop('rank', None)
        self.popularity = kwargs.pop('popularity', None)
        self.members = kwargs.pop('members', None)
        self.favorites = kwargs.pop('favorites', None)

        self.related = []
        self._raw_related = kwargs.pop('related', None)
        for relation_type, relations in self._raw_related.items():
            for relation in relations:
                relation['relation'] = relation_type
                obj = create_relation(relation)
                self.related.append(obj)
