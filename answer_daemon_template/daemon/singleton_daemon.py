# -*- coding: utf-8 -*-

from answer_daemon_template.daemon.daemon import Daemon


class SingletonDaemon:

    __singleton_instance__: Daemon

    @classmethod
    def get(cls) -> Daemon:
        if not hasattr(cls, "__singleton_instance__"):
            setattr(cls, "__singleton_instance__", Daemon())
        return cls.__singleton_instance__

    def __init__(self):
        pass
