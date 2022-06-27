# -*- coding: utf-8 -*-

from unittest import TestCase, main

from answer_daemon_template.daemon.singleton_daemon import SingletonDaemon


class SingletonDaemonTestCase(TestCase):
    def test_attribute_error(self):
        with self.assertRaises(AttributeError):
            SingletonDaemon.get()

    def test_create_and_destroy(self):
        self.assertIsNotNone(SingletonDaemon.create(object()))  # noqa
        self.assertIsNotNone(SingletonDaemon.get())

        SingletonDaemon.destroy()
        with self.assertRaises(AttributeError):
            SingletonDaemon.get()

    def test_same_instance(self):
        self.assertIsNotNone(SingletonDaemon.create(object()))  # noqa
        instance1 = SingletonDaemon.get()
        instance2 = SingletonDaemon.get()
        self.assertEqual(instance1, instance2)
        SingletonDaemon.destroy()


if __name__ == "__main__":
    main()
