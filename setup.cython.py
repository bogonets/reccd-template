# -*- coding: utf-8 -*-

from setup_utils import (
    SPECIAL_DUNDER_FILE_PATTERNS,
    default_compile_files,
    default_package_data,
    default_packages,
    default_requirements,
    default_version,
    filter_match,
)
from setup_variables import PACKAGE_NAME
from setuptools import setup
from setuptools.command.build_py import build_py

# noinspection PyPackageRequirements
from Cython.Build import cythonize  # isort:skip


class NoPythonBuildPy(build_py):
    def find_package_modules(self, package, package_dir):
        # ext_suffix = sysconfig.get_config_var("EXT_SUFFIX")
        modules = super().find_package_modules(package, package_dir)
        filtered_modules = []
        for pkg, mod, filepath in modules:
            if filter_match(filepath, SPECIAL_DUNDER_FILE_PATTERNS):
                filtered_modules.append((pkg, mod, filepath))
        return filtered_modules


def default_cython_modules(no_debugging_symbols=True):
    cython_modules = cythonize(
        module_list=default_compile_files(),
        compiler_directives={"language_level": 3},
    )
    if no_debugging_symbols:
        for ext in cython_modules:
            ext.extra_compile_args = ["-g0"]
    return cython_modules


def setup_main():
    setup(
        name=PACKAGE_NAME,
        version=default_version(),
        packages=default_packages(),
        ext_modules=default_cython_modules(),
        cmdclass={"build_py": NoPythonBuildPy},  # noqa
        package_dir={PACKAGE_NAME: PACKAGE_NAME},
        package_data={PACKAGE_NAME: default_package_data()},
        install_requires=default_requirements(),
    )


if __name__ == "__main__":
    setup_main()
