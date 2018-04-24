"""Partial Classes"""

import tokage


class BasePartial:
    def __init__(self, *args, **kwargs):
        self.__id = kwargs.get("id")
        self.__type = self.__class__.__name__.split("Partial")[1].lower()
        self.__state = kwargs.get("state")

    async def request_full(self):
        """Request an instance of the full, non-partial class. For example, :class:`PartialAnime` -> :class:`Anime`"""
        return await getattr(self.__state, "get_" + self.__type)(self.__id)


class PartialAnime(BasePartial):
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
    def __init__(self, title, id, url, **kwargs):
        self.title = title
        self.id = int(id)
        self.url = url
        self.relation = kwargs.get("relation")
        super().__init__(id=id, state=kwargs.get("state"))

    @classmethod
    def from_related(cls, data, **kwargs):
        title = data.get('title')
        id = int(data.get('mal_id'))
        url = data.get('url')
        relation = data.get('relation')
        return cls(title, id, url, relation=relation, state=kwargs.get("state"))

    @classmethod
    def from_character(cls, data, **kwargs):
        title = data.get('name')
        id = int(data.get('mal_id'))
        url = data.get('url')
        return cls(title, id, url, state=kwargs.get("state"))


class PartialManga(BasePartial):
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
    def __init__(self, title, id, url, **kwargs):
        self.title = title
        self.id = int(id)
        self.url = url
        self.relation = kwargs.get("relation")
        super().__init__(id=id, state=kwargs.get("state"))

    @classmethod
    def from_related(cls, data, **kwargs):
        title = data.get('title')
        id = int(data.get('mal_id'))
        url = data.get('url')
        relation = data.get('relation')
        return cls(title, id, url, relation=relation, state=kwargs.get("state"))

    @classmethod
    def from_character(cls, data, **kwargs):
        title = data.get('name')
        id = int(data.get('mal_id'))
        url = data.get('url')
        return cls(title, id, url, state=kwargs.get("state"))


class PartialPerson(BasePartial):
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
    def __init__(self, name, id, url, **kwargs):
        self.name = name
        self.id = int(id)
        self.url = url
        self.language = kwargs.get("language")
        super().__init__(id=id, state=kwargs.get("state"))

    @classmethod
    def from_voice_acting(cls, data, **kwargs):
        name = data.get('name')
        id = int(data.get('mal_id'))
        url = data.get('url')
        lang = data.get('language')
        return cls(name, id, url, language=lang, state=kwargs.get("state"))

    @classmethod
    def from_author(cls, data, **kwargs):
        name = data.get('name')
        id = int(data.get('mal_id'))
        url = data.get('url')
        return cls(name, id, url, state=kwargs.get("state"))


class PartialCharacter(BasePartial):
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
    def __init__(self, name, id, url, **kwargs):
        self.name = name
        self.id = int(id)
        self.url = url
        self.anime = kwargs.get("anime")
        super().__init__(id=id, state=kwargs.get("state"))

    @classmethod
    def from_person(cls, data, anime, **kwargs):
        name = data.get('name')
        id = int(data.get('mal_id'))
        url = data.get('url')
        return cls(name, id, url, anime=anime, state=kwargs.get("state"))

    @classmethod
    def from_search(cls, data, **kwargs):
        name = data['name']
        url = data['url']
        id = tokage.utils.parse_id(url)
        return cls(name, id, url, state=kwargs.get("state"))
