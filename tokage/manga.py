"""Manga object"""

from .utils import create_relation, parse_id
from .partial import PartialPerson


class Manga:
    """Represents a MAL Manga (Includes Novels)

    Attributes
    ----------
    id : int
        The Manga's ID.

    title : str
        The Series title.

    type : str
       The Manga's type. Can be either "Novel" or "Manga".

    synonyms : list[str]
       Alternative names for the Manga.

    image : str
        The cover image URL for the Manga.

    japanese_title : str
        Japanese title of the Manga.

    status : str
        Publishing status of the Manga.

    volumes : int
        Volume count of the Manga.

    chapters : int
        Chapter count of the Manga.

    publish_start : str
        Publication start date.

    publish_end : str
        Publication end date.

    publishing : bool
        True if the manga is publishing, False if not.

    synopsis : str
        Description of the Manga.

    author : :class:`PartialPerson`
        PartialPerson instance of the Manga author.

    serialization : str
        The Manga's serialization.

    genres : list[str]
        List of the Manga's genres.

    link : str
        Link to the Manga on MAL.

    score : tuple(int)
        Tuple of (score, voters).

    rank : int
        Manga's rank on the MAL board.

    popularity : int
        Popularity rank of the Manga.

    members : int
        Amount of members which have the Manga in their list.

    favorites : int
        Amount of favorites given to the Manga.

    related : list[:class:`.PartialAnime` or :class:`.PartialManga`]
        List of related Anime or Manga.

    """

    def __init__(self, manga_id, **kwargs):
        self.id = manga_id
        self.title = kwargs.pop('title', None)
        self.type = kwargs.pop('type', None)
        self.synonyms = kwargs.pop('title_synonyms', None)
        self.image = kwargs.pop('image_url', None)
        self.japanese_title = kwargs.pop('title_japanese', None)
        self.status = kwargs.pop('status', None)
        self.volumes = kwargs.pop('volumes', None)
        self.chapters = kwargs.pop('chapters', None)
        self.publishing = kwargs.pop('publishing', None)
        self.synopsis = kwargs.pop('synopsis', None)

        self._publish_time = kwargs.pop('published_string', None)
        if " to " not in self._publish_time:
            self.publish_start = self._publish_time
            self.publish_end = None
        else:
            self.publish_start, self.publish_end = self._publish_time.split(" to ")

        self._raw_author = kwargs.pop('author', None)[0]
        self._raw_author['id'] = parse_id(self._raw_author['url'])
        self.author = PartialPerson.from_author(self._raw_author)

        self._raw_genres = kwargs.pop('genre', None)
        if self._raw_genres is None:
            self._raw_genres = kwargs.pop('genres', None)
        self.genres = [g['name'] for g in self._raw_genres] if self._raw_genres else None

        self.serialization = kwargs.pop('serialization', None)[0]  # TODO: add serializations
        self.link = kwargs.pop('link_canonical', None)
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
