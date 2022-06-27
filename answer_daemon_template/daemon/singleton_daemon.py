# -*- coding: utf-8 -*-

from answer_daemon_template.daemon.daemon import Daemon


class SingletonDaemon:

    __singleton_instance__: Daemon

    @classmethod
    def create(cls) -> Daemon:
        cls.__singleton_instance__ = Daemon()
        return cls.__singleton_instance__

    @classmethod
    def destroy(cls) -> None:
        del cls.__singleton_instance__

    @classmethod
    def get(cls) -> Daemon:
        return cls.__singleton_instance__

    def __init__(self):
        pass
