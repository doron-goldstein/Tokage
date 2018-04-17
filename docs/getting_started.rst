.. currentmodule:: tokage

Getting Started
===============

Installing
----------

You can install Tokage using pip:
::

    pip install -U tokage



Usage
-----

Tokage is an *asynchronous* library.
This means you must use some kind of async library to handle the HTTP requests to the API.

Tokage supports asyncio, which is provided in the standard python library.
Additionally, Tokage also supports `curio <https://github.com/dabeaz/curio>`_ and `trio <https://github.com/python-trio/trio>`_, two awesome libraries which solve many of the problems asyncio has.
If you prefer, you may also use `multio <https://github.com/theelous3/multio>`_, a library that brings the two together

Whichever you prefer, tokage will adapt to it. For more info on how to use each type of library, refer to the examples below.

Examples
--------

Basic Asyncio Example
~~~~~~~~~~~~~~~~~~~~~

::

    import asyncio
    import tokage

    async def main():
        client = tokage.Client() # Create a new Client instance. Default lib is asyncio.

        anime_id = await client.search_id("anime", "Steins Gate")  # Search for an ID of an Anime called "Steins gate"
        anime = await client.get_anime(anime_id)  # Get the Anime object from the API

        manga_id = await client.search_id("manga", "my hero academia")  # Search for an ID of a Manga called "my hero academia"
        manga = await client.get_manga(manga_id)  # Get the Manga object from the API

        print("Anime title:", anime.title)  # Print the title of the Anime
        print("Manga title:", manga.title)  # Print the title of the Manga

        await client.cleanup()  # Finally, clean up

    loop = asyncio.get_event_loop() # Get the event loop
    loop.run_until_complete(main()) # Run main

Prints:
::

    Anime title: Steins;Gate
    Manga title: Boku no Hero Academia


Basic Curio Example
~~~~~~~~~~~~~~~~~~~

::

    import curio
    import tokage

    async def main():
        client = tokage.Client(lib='curio')  # Create a client instance. Tell tokage to use curio

        anime = await client.get_anime(1)  # Get the Anime with ID `1`, which is Cowboy Bebop

        print("Anime title:", anime.title)  # Print the title and premiere season of the Anime
        print("Started airing:", anime.premiered)

        await client.cleanup()  # Finally, clean up (currently, this does nothing in curio/trio mode, so it can be omitted)

    curio.run(main)  # Run main

Prints:
::

    Anime title: Cowboy Bebop
    Started airing: Spring 1998


Basic Trio Example
~~~~~~~~~~~~~~~~~~

::

    import trio
    import tokage

    async def main():
        client = tokage.Client(lib='trio')  # Create a client instance. Tell tokage to use trio

        anime = await client.get_anime(1)  # Get the Anime with ID `1`, which is Cowboy Bebop

        print("Anime title:", anime.title)  # Print the title and premiere season of the Anime
        print("Started airing:", anime.premiered)

        await client.cleanup()  # Finally, clean up (currently, this does nothing in curio/trio mode, so it can be omitted)

    trio.run(main)  # Run main

Prints:
::

    Anime title: Cowboy Bebop
    Started airing: Spring 1998


Basic Multio Example
~~~~~~~~~~~~~~~~~~~~

::

    import multio
    import tokage

    multio.init('trio')  # initiate multio to use trio. Also works the same with curio

    async def main():
        client = tokage.Client(lib='trio')  # Create a client instance. Tell tokage to use trio

        anime = await client.get_anime(1)  # Get the Anime with ID `1`, which is Cowboy Bebop

        print("Anime title:", anime.title)  # Print the title and premiere season of the Anime
        print("Started airing:", anime.premiered)

        await client.cleanup()  # Finally, clean up (currently, this does nothing in curio/trio mode, so it can be omitted)

    multio.run(main)  # Run main

Prints:
::

    Anime title: Cowboy Bebop
    Started airing: Spring 1998


