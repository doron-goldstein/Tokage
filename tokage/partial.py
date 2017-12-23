"""Partial Classes"""


class PartialAnime:
    def __init__(self, title, id, url, relation=None):
        self.title = title
        self.id = id
        self.url = url
        self.relation = relation

    @classmethod
    def from_related(cls, kwargs):
        title = kwargs.get('title')
        id = kwargs.get('mal_id')
        url = kwargs.get('url')
        relation = kwargs.get('relation')
        return cls(title, id, url, relation)

    @classmethod
    def from_character(cls, kwargs):
        title = kwargs.get('name')
        id = kwargs.get('id')
        url = kwargs.get('url')
        return cls(title, id, url)


class PartialManga:
    def __init__(self, title, id, url, relation=None):
        self.title = title
        self.id = id
        self.url = url
        self.relation = relation

    @classmethod
    def from_related(cls, kwargs):
        title = kwargs.get('title')
        id = kwargs.get('mal_id')
        url = kwargs.get('url')
        relation = kwargs.get('relation')
        return cls(title, id, url, relation)

    @classmethod
    def from_character(cls, kwargs):
        title = kwargs.get('name')
        id = kwargs.get('id')
        url = kwargs.get('url')
        return cls(title, id, url)


class PartialPerson:
    def __init__(self, name, id, url):
        self.name = name
        self.id = id
        self.url = url

    @classmethod
    def from_author(cls, kwargs):
        name = kwargs.get('name')
        id = kwargs.get('id')
        url = kwargs.get('url')
        return cls(name, id, url)


class PartialCharacter:
    ...
