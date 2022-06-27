# -*- coding: utf-8 -*-

from typing import Callable, List, Tuple


class Daemon:
    def __init__(self):
        pass

    async def on_open(self) -> None:
        pass

    async def on_close(self) -> None:
        pass

    def on_routes(self) -> List[Tuple[str, str, Callable]]:
        assert self
        return []
