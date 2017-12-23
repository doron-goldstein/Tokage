"""Person object"""


class Person:
    """Represents a MAL Person (Voice Actors, Staff, etc.)

    Attributes
    ----------
    id : int
        The Person's ID.

    name : str
        The Person's name.

    link : str
        Link to the Person on MAL.

    image : str
        Image URL of the Person.

    favorites : int
        Amount of favorites the Person has.

    anime : list[dict]
        WIP - Staff positions in Anime.

    manga : list[dict]
        WIP - Published Manga.

    more : str
        Additional info about the Person.

    website : str
        Link to the Person's website

    voice_acting : list[dict]
        WIP - List of voice acting roles the Person has.

    """

    def __init__(self, person_id, **kwargs):
        self.id = person_id
        self.link = kwargs.pop('link_canonical', None)
        self.name = kwargs.pop('name', None)
        self.image = kwargs.pop('image_url', None)
        self.favorites = kwargs.pop('member_favorites', None)
        self.anime = kwargs.pop('anime_staff_position', None)  # TODO: Handle
        self.manga = kwargs.pop('published_manga', None)  # TODO: Handle
        self.birthday = kwargs.pop('birthday', None)
        self.more = kwargs.pop('more', None)
        self.website = kwargs.pop('website', None)
        self.voice_acting = kwargs.pop('voice_acting_role', None)  # TODO: Handle
