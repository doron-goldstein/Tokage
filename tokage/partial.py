"""Partial Classes"""

from .utils import parse_id


class PartialAnime:
    """Represents a part of an Anime object

    Attributes
    ----------

    title : str
        The Anime's title.

    id : int
        The Anime's ID.

    url : str
        Link to the Anime.

    relation : Optional[str]
        relation of the anime to a :class:`Person` or an :class:`Anime`.

    """
    def __init__(self, title, id, url, relation=None):
        self.title = title
        self.id = int(id)
        self.url = url
        self.relation = relation

    @classmethod
    def from_related(cls, data):
        title = data.get('title')
        id = int(data.get('mal_id'))
        url = data.get('url')
        relation = data.get('relation')
        return cls(title, id, url, relation)

    @classmethod
    def from_character(cls, data):
        title = data.get('name')
        id = int(data.get('id'))
        url = data.get('url')
        return cls(title, id, url)


class PartialManga:
    """Represents a part of a Manga object

    Attributes
    ----------

    title : str
        The Manga's title.

    id : int
        The Manga's ID.

    url : str
        Link to the Manga.

    relation : Optional[str]
        relation of the manga to a :class:`Person` or a :class:`Manga`.

    """
    def __init__(self, title, id, url, relation=None):
        self.title = title
        self.id = int(id)
        self.url = url
        self.relation = relation

    @classmethod
    def from_related(cls, data):
        title = data.get('title')
        id = int(data.get('mal_id'))
        url = data.get('url')
        relation = data.get('relation')
        return cls(title, id, url, relation)

    @classmethod
    def from_character(cls, data):
        title = data.get('name')
        id = int(data.get('id'))
        url = data.get('url')
        return cls(title, id, url)


class PartialPerson:
    """Represents a part of a Person object

    Attributes
    ----------

    name : str
        The Person's name.

    id : int
        The Person's ID.

    url : str
        Link to the Person.

    language : Optional[str]
        If this is a partial voice actor, the language of the voice acting.

    """
    def __init__(self, name, id, url, language=None):
        self.name = name
        self.id = int(id)
        self.url = url
        self.language = language

    @classmethod
    def from_voice_acting(cls, data):
        name = data.get('name')
        id = int(data.get('id'))
        url = data.get('url')
        lang = data.get('language')
        return cls(name, id, url, lang)

    @classmethod
    def from_author(cls, data):
        name = data.get('name')
        id = int(data.get('id'))
        url = data.get('url')
        return cls(name, id, url)


class PartialCharacter:
    """Represents a part of a Character object

    Attributes
    ----------

    name : str
        The Character's name.

    id : int
        The Character's ID.

    url : str
        Link to the Character.

    anime : Optional[:class:`PartialAnime`]
        The anime this character is from.

    """
    def __init__(self, name, id, url, anime=None):
        self.name = name
        self.id = int(id)
        self.url = url
        self.anime = anime

    @classmethod
    def from_person(cls, data, anime):
        name = data.get('name')
        id = int(data.get('id'))
        url = data.get('url')
        return cls(name, id, url, anime)

    @classmethod
    def from_search(cls, data):
        name = data['name']
        url = data['url']
        id = parse_id(url)
        return cls(name, id, url)

