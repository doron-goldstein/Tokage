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
        self.link = kwargs.get('link_canonical')
        self.name = kwargs.get('name')
        self.image = kwargs.get('image_url')
        self.favorites = kwargs.get('member_favorites')
        self.anime = kwargs.get('anime_staff_position')  # TODO: Handle
        self.manga = kwargs.get('published_manga')  # TODO: Handle
        self.birthday = kwargs.get('birthday')
        self.more = kwargs.get('more')
        self.website = kwargs.get('website')
        self.voice_acting = kwargs.get('voice_acting_role')  # TODO: Handle
