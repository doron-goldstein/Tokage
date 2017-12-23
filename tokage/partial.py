"""Partial Classes"""


class PartialAnime:
    @classmethod
    def from_relation(self):
        ...

    @classmethod
    def from_anime(self):
        ...


class PartialManga:
    @classmethod
    def from_relation(self):
        ...

    @classmethod
    def from_manga(self):
        ...


class PartialPerson:
    @classmethod
    def from_anime(self):
        ...


class PartialCharacter:
    ...
