# -*- coding: utf-8 -*-

from typing import Callable, List, Tuple

from answer_daemon_template.daemon.singleton_daemon import SingletonDaemon

__version__ = "0.0.1"
"""
The daemon version must be specified. Use the semantic versioning specification.
e.g. `MAJOR.MINOR.PATCH`
"""

__doc__ = "Answer Daemon Template Project"
"""
The daemon's documentation string.
"""

__recc_spec__ = {}
"""
A specification dictionary for the recc plugin.
"""


def on_create() -> None:
    """
    Called immediately after the application launch process completes.
    """
    SingletonDaemon.create()


def on_destroy() -> None:
    """
    Called just before the application exit process.
    """
    SingletonDaemon.destroy()


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


async def on_create_group(uid: int) -> None:
    """
    Called when a group is created.
    """
    await SingletonDaemon.get().on_create_group(uid)


async def on_delete_group(uid: int) -> None:
    """
    Called when a group is deleted.
    """
    await SingletonDaemon.get().on_delete_group(uid)


async def on_create_project(uid: int) -> None:
    """
    Called when a project is created.
    """
    await SingletonDaemon.get().on_create_project(uid)


async def on_delete_project(uid: int) -> None:
    """
    Called when a project is deleted.
    """
    await SingletonDaemon.get().on_delete_project(uid)


def on_routes() -> List[Tuple[str, str, Callable]]:
    """
    It should return a routing table that can accept HTTP requests.
    """
    return SingletonDaemon.get().on_routes()


if __name__ == "__main__":
    # If you need to run it standalone.
    pass
