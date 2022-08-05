# -*- coding: utf-8 -*-

from typing import Callable, List, Tuple

__version__ = "0.0.2"
"""
The plug-in version must be specified. Use the semantic versioning specification.
e.g. `MAJOR.MINOR.PATCH`
"""

__doc__ = "Documentation"
"""
The module's documentation string.
"""


async def on_open() -> None:
    """
    An asynchronous constructor event that runs in the main event loop.
    """
    print("Module 'open' event")


async def on_close() -> None:
    """
    An asynchronous destructor event that runs in the main event loop.
    """
    print("Module 'close' event")


async def post_echo(msg: str) -> str:
    print(f"Echo message:'{msg}'")
    return msg


def on_routes() -> List[Tuple[str, str, Callable]]:
    """
    It should return a routing table that can accept HTTP requests.
    """
    return [
        ("POST", "/echo", post_echo),
    ]


if __name__ == "__main__":
    # If you need to run it standalone.
    pass
