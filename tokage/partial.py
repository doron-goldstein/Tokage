"""Partial Classes"""


class Relation:
    def __init__(self, *args):
        ...


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


class PartialPerson:
    @classmethod
    def from_anime(self):
        ...


class PartialCharacter:
    ...
