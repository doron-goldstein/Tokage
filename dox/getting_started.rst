.. currentmodule:: tokage

Getting Started
===============

Installing
----------

You can install Tokage using pip:
::

    pip install -U tokage



Examples
--------

Basic Example
~~~~~~~~~~~~~

::

    import asyncio
    import tokage

    async def main()
        client = tokage.Client() # Create a new Client instance.
        
        anime_id = await client.search_id("anime", "Steins Gate") # Search for an ID of an Anime called "Steins gate"
        anime = await client.get_anime(anime_id) # Get the Anime object from the API
    
        manga_id = await client.search_id("manga", "my hero academia") # Search for an ID of a Manga called "my hero academia"
        manga = await client.get_manga(manga_id) # Get the Manga object from the API

        print("Anime title: {}".format(anime.title)) # Print the title of the Anime
        print("Manga title: {}".format(manga.title)) # Print the title of the Manga
    
    loop = asyncio.get_event_loop() # Get the event loop
    loop.run_until_complete(main()) # Run main

Prints:
::

    Anime title: Steins;Gate
    Manga title: Boku no Hero Academia