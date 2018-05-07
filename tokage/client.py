import json
from html.parser import HTMLParser
from urllib.parse import parse_qs

from lxml import etree

from tokage.anime import Anime
from tokage.character import Character
from tokage.errors import *  # noqa
from tokage.manga import Manga
from tokage.person import Person
from tokage.utils import parse_id
from tokage.partial import *  # noqa

BASE_URL = 'https://api.jikan.moe/'
ANIME_URL = BASE_URL + 'anime/'
MANGA_URL = BASE_URL + 'manga/'
PERSON_URL = BASE_URL + 'person/'
CHARACTER_URL = BASE_URL + 'character/'
SEARCH_URL = BASE_URL + 'search/'


class Client:
    """Client connection to the MAL API.
    This class is used to interact with the API.

    Parameters
    ----------
    session : Optional[Union[aiohttp.ClientSession, asks.Session]]

        The session to use for aiohttp/asks requests.

        Defaults to creating a new one.

    lib : Optional[str]

        The async library to use Tokage with. Defaults to `asyncio`.
        Valid libraries: `asyncio`, `multio`.

    loop : Optional[asyncio.BaseEventLoop]

        For use with `asyncio`. The event loop to use for `aiohttp`.

        Defaults to creating a new one.

    Attributes
    ----------
    session : Union[aiohttp.ClientSession, asks.Session]

        The session used for aiohttp/asks HTTP requests.

    """
    def __init__(self, session=None, *, lib='asyncio', loop=None):
        if lib not in ('asyncio', 'multio'):
            raise ValueError("lib must be of type `str` and be either `asyncio` or `multio`, "
                             "not `{}`".format(lib if isinstance(lib, str) else lib.__class__.__name__))
        self._lib = lib
        if lib == 'asyncio':
            import asyncio
            loop = loop or asyncio.get_event_loop()
        self.session = session or self._make_session(lib, loop)
        self._html_parser = HTMLParser()

    @staticmethod
    def _make_session(lib, loop=None):
        if lib == 'asyncio':
            try:
                import aiohttp
            except ImportError:
                raise ImportError("To use tokage in asyncio mode, it requires the `aiohttp` module.")
            return aiohttp.ClientSession(loop=loop)
        try:
            import asks
        except ImportError:
            raise ImportError("To use tokage in curio/trio mode, it requires the `asks` module.")
        return asks.Session()

    async def cleanup(self):
        if self._lib == 'asyncio':
            await self.session.close()

    async def _json(self, resp, encoding=None):
        """Read, decodes and unescapes a JSON `aiohttp.ClientResponse` object."""
        def unescape_json(json_data):
            if isinstance(json_data, str):
                return self._html_parser.unescape(json_data)
            if isinstance(json_data, list):
                return [unescape_json(i) for i in json_data]
            if isinstance(json_data, dict):
                return {
                    unescape_json(k): unescape_json(v)
                    for k, v in json_data.items()
                }
            return json_data

        if self._lib == 'asyncio':
            if resp._content is None:
                await resp.read()
                stripped = resp._content.strip()
        else:
            stripped = resp.content.strip()

        if not stripped:
            return None

        if encoding is None:
            if self._lib == 'asyncio':
                encoding = resp._get_encoding()
            else:
                encoding = resp.encoding

        json_resp = json.loads(stripped.decode(encoding))

        return unescape_json(json_resp)

    async def request(self, url):
        resp = await self.session.get(url)
        return await self._json(resp)

    async def get_anime(self, target_id):
        """Retrieves an :class:`Anime` object from an ID

        Raises a :class:`AnimeNotFound` Error if an Anime was not found corresponding to the ID.
        """
        resp = await self.request(ANIME_URL + str(target_id))
        if resp is None:
            raise AnimeNotFound("Anime with the given ID was not found")
        result = Anime(target_id, resp, state=self)
        return result

    async def get_manga(self, target_id):
        """Retrieves a :class:`Manga` object from an ID

        Raises a :class:`MangaNotFound` Error if a Manga was not found corresponding to the ID.
        """
        resp = await self.request(MANGA_URL + str(target_id))
        if resp is None:
            raise MangaNotFound("Manga with the given ID was not found")
        result = Manga(target_id, resp, state=self)
        return result

    async def get_character(self, target_id):
        """Retrieves a :class:`Character` object from an ID

        Raises a :class:`CharacterNotFound` Error if a Character was not found corresponding to the ID.
        """
        resp = await self.request(CHARACTER_URL + str(target_id))
        if resp is None:
            raise CharacterNotFound("Character with the given ID was not found")
        result = Character(target_id, resp, state=self)
        return result

    async def get_person(self, target_id):
        """Retrieves a :class:`Person` object from an ID

        Raises a :class:`PersonNotFound` Error if a Person was not found corresponding to the ID.
        """
        resp = await self.request(PERSON_URL + str(target_id))
        if resp is None:
            raise PersonNotFound("Person with the given ID was not found")
        result = Person(target_id, resp, state=self)
        return result

    async def search_anime(self, query):
        """Search for :class:`PartialAnime` by query.

        Returns a list of results.
        """
        resp = await self.request(SEARCH_URL + "anime/" + query)
        if resp is None or not resp['result']:
            raise AnimeNotFound("Anime `{}` could not be found".format(query))
        return [PartialAnime(a['title'], a['mal_id'], a['url'], state=self) for a in resp['result']]

    async def search_manga(self, query):
        """Search for :class:`PartialManga` by query.

        Returns a list of results.
        """
        resp = await self.request(SEARCH_URL + "manga/" + query)
        if resp is None or not resp['result']:
            raise MangaNotFound("Manga `{}` could not be found".format(query))
        return [PartialManga(m['title'], m['mal_id'], m['url'], state=self) for m in resp['result']]

    async def search_character(self, query):
        """Search for :class:`PartialCharacter` by query.

        Returns a list of results.
        """
        resp = await self.request(SEARCH_URL + "character/" + query)
        if resp is None or not resp['result']:
            raise CharacterNotFound("Character `{}` could not be found".format(query))
        return [PartialCharacter.from_search(c, state=self) for c in resp['result']]

    async def search_person(self, query):
        """Search for :class:`PartialPerson` by query.

        Returns a list of results.
        """
        resp = await self.request(SEARCH_URL + "person/" + query)
        if resp is None or not resp['result']:
            raise PersonNotFound("Person `{}` could not be found".format(query))
        return [PartialPerson(p['name'], p['mal_id'], p['url'], state=self) for p in resp['result']]

    async def search_id(self, type_, query):
        """Parse a google query and return the ID.

        Raises a :class:`TokageNotFound` Error if an ID was not found.
        """
        query = "site:myanimelist.net/{}/ {}".format(type_, query)
        params = {
            'q': query,
            'safe': 'on'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'
        }

        url = 'https://www.google.com/search'
        async with self.session.get(url, params=params, headers=headers) as resp:
            if resp.status != 200:
                raise RuntimeError('Google somehow failed to respond.')

            root = etree.fromstring(await resp.text(), etree.HTMLParser())
            nodes = root.findall(".//div[@class='g']")
            for node in nodes:
                url_node = node.find('.//h3/a')
                if url_node is None:
                    continue

                url = url_node.attrib['href']
                if not url.startswith('/url?'):
                    continue

                url = parse_qs(url[5:])['q'][0]
                id = parse_id(url)
                if id is None:
                    raise TokageNotFound("An ID corresponding to the given query was not found")
                return id

            else:
                raise TokageNotFound("An ID corresponding to the given query was not found")
