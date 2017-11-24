
Tokage
======

Tokage is an async wrapper for the `MAL <https://myanimelist.net/>`_ API.
This wrapper is compatible with Python 3.5+ and uses `Jikan <http://jikan.me/>`_ as an alternative to the default MAL API.

Documentation can be found `here <http://tokage.readthedocs.io/en/latest/index.html>`_.

This wrapper is aimed at ease of use and an object-oriented style.

Example
-------

::

    import asyncio
    import tokage

    async def main():
        client = tokage.Client()  # Create a new Client instance
        
        anime_id = await client.search_id("anime", "re zero")  # Search for an ID
        anime = await client.get_anime(anime_id)  # Get the Anime object from the API
    
        print("Anime title: {}".format(anime.title))  # Print the title of the Anime
        await client.cleanup()  # cleanup after everything
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main()) # Run main

Prints:
::

    Anime title: Re:Zero kara Hajimeru Isekai Seikatsu

