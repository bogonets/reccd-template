# -*- coding: utf-8 -*-

from typing import Callable, List, Tuple

from answer_daemon_template.daemon.singleton_daemon import SingletonDaemon


async def on_open() -> None:
    """
    An asynchronous constructor event that runs in the main event loop.
    """
    await SingletonDaemon.get().on_open()


async def on_close() -> None:
    """
    An asynchronous destructor event that runs in the main event loop.
    """
    await SingletonDaemon.get().on_close()


def on_routes() -> List[Tuple[str, str, Callable]]:
    """
    It should return a routing table that can accept HTTP requests.
    """
    return SingletonDaemon.get().on_routes()


if __name__ == "__main__":
    # If you need to run it standalone.
    pass
