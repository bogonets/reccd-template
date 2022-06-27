# -*- coding: utf-8 -*-

from setup_utils import (
    PACKAGE_NAME,
    default_package_data,
    default_packages,
    default_requirements,
    default_version,
)
from setuptools import setup


def setup_main():
    setup(
        name=PACKAGE_NAME,
        version=default_version(),
        packages=default_packages(),
        package_dir={PACKAGE_NAME: PACKAGE_NAME},
        package_data={PACKAGE_NAME: default_package_data()},
        install_requires=default_requirements(),
    )


if __name__ == "__main__":
    setup_main()
