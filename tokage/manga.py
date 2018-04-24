"""Manga object"""

import tokage
from tokage.partial import PartialPerson
from tokage.utils import create_relation, parse_id


class Manga(tokage.TokageBase):
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

    def __init__(self, manga_id, data, **kwargs):
        self.id = manga_id
        self.title = data.get('title')
        self.type = data.get('type')
        self.synonyms = data.get('title_synonyms')
        self.image = data.get('image_url')
        self.japanese_title = data.get('title_japanese')
        self.status = data.get('status')
        self.volumes = data.get('volumes')
        self.chapters = data.get('chapters')
        self.publishing = data.get('publishing')
        self.synopsis = data.get('synopsis')

        self._publish_time = data.get('published_string')
        if " to " not in self._publish_time:
            self.publish_start = self._publish_time
            self.publish_end = None
        else:
            self.publish_start, self.publish_end = self._publish_time.split(" to ")

        self._raw_author = data.get('author')[0]
        self._raw_genres = data.get('genre') or data.get('genres')
        self.serialization = data.get('serialization')[0]  # TODO: add serializations
        self.link = data.get('link_canonical')
        self.score = data.get('score')
        self.rank = data.get('rank')
        self.popularity = data.get('popularity')
        self.members = data.get('members')
        self.favorites = data.get('favorites')
        self._raw_related = data.get('related')
        super().__init__(state=kwargs.get("state"))

    @property
    def author(self):
        self._raw_author['mal_id'] = parse_id(self._raw_author['url'])
        return PartialPerson.from_author(self._raw_author, state=self._state)

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
