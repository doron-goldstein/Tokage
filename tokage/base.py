"""Base class for content types"""


class TokageBase:
    def __init__(self, *args, **kwargs):
        self._state = kwargs.get("state")
