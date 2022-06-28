# -*- coding: utf-8 -*-

from unittest import TestCase, main

from answer_daemon_template.daemon.singleton_daemon import SingletonDaemon


class SingletonDaemonTestCase(TestCase):
    def test_same_instance(self):
        instance1 = SingletonDaemon.get()
        instance2 = SingletonDaemon.get()
        self.assertEqual(instance1, instance2)


if __name__ == "__main__":
    main()
