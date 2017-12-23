"""Partial Classes"""


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

    """
    def __init__(self, title, id, url, relation=None):
        self.title = title
        self.id = int(id)
        self.url = url
        self.relation = relation

    @classmethod
    def from_related(cls, kwargs):
        title = kwargs.get('title')
        id = int(kwargs.get('mal_id'))
        url = kwargs.get('url')
        relation = kwargs.get('relation')
        return cls(title, id, url, relation)

    @classmethod
    def from_character(cls, kwargs):
        title = kwargs.get('name')
        id = int(kwargs.get('id'))
        url = kwargs.get('url')
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

    """
    def __init__(self, title, id, url, relation=None):
        self.title = title
        self.id = int(id)
        self.url = url
        self.relation = relation

    @classmethod
    def from_related(cls, kwargs):
        title = kwargs.get('title')
        id = int(kwargs.get('mal_id'))
        url = kwargs.get('url')
        relation = kwargs.get('relation')
        return cls(title, id, url, relation)

    @classmethod
    def from_character(cls, kwargs):
        title = kwargs.get('name')
        id = int(kwargs.get('id'))
        url = kwargs.get('url')
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

    """
    def __init__(self, name, id, url):
        self.name = name
        self.id = int(id)
        self.url = url

    @classmethod
    def from_author(cls, kwargs):
        name = kwargs.get('name')
        id = int(kwargs.get('id'))
        url = kwargs.get('url')
        return cls(name, id, url)


class PartialCharacter:
    ...
