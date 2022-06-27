# -*- coding: utf-8 -*-

import os
import re
from typing import Iterable, List

from setup_variables import (
    PACKAGE_DATA_NAMES,
    PACKAGE_NAME,
    README_NAME,
    REQUIREMENTS_NAME,
    VERSION_REGEX,
)
from setuptools import find_packages

SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
PACKAGE_DIR = os.path.join(SCRIPT_DIR, PACKAGE_NAME)
PACKAGE_INIT_PY = os.path.join(PACKAGE_DIR, "__init__.py")
README_PATH = os.path.join(SCRIPT_DIR, README_NAME)
REQUIREMENTS = os.path.join(SCRIPT_DIR, REQUIREMENTS_NAME)

SPECIAL_DUNDER_FILE_PATTERNS = (
    re.compile(r".*__init__\.py$"),
    re.compile(r".*__main__\.py$"),
)
PYTHON_CACHE_DIRECTORY_PATTERNS = (re.compile(r"(^|.*/)?__pycache__($|/.*)"),)
PACKAGE_DATA_IGNORE_PATTERNS = (
    SPECIAL_DUNDER_FILE_PATTERNS + PYTHON_CACHE_DIRECTORY_PATTERNS
)


def read_file(path: str, encoding="utf-8") -> str:
    with open(path, encoding=encoding) as f:
        return f.read()


def read_version(path: str, encoding="utf-8") -> str:
    content = read_file(path, encoding)
    matches = re.search(VERSION_REGEX, content, re.M)
    if not matches:
        raise RuntimeError(f"Unable to find version string in {PACKAGE_INIT_PY}")
    return matches.group(1)


def read_requirements(path: str, encoding="utf-8") -> List[str]:
    content = read_file(path, encoding)
    lines0 = content.split("\n")
    lines1 = map(lambda x: x.strip(), lines0)
    lines2 = filter(lambda x: x and x[0] != "#", lines1)
    return list(lines2)


def filter_ignore(sources: Iterable[str], patterns: Iterable[re.Pattern]) -> List[str]:
    result = list(sources)
    for p in patterns:
        result = list(filter(lambda x: p.match(x) is None, result))
    return result


def children_files(path: str) -> List[str]:
    result = []
    for parent, _, files in os.walk(path):
        for name in files:
            result.append(os.path.join(parent, name))
    return result


def match_files(path: str, regexp=r".*") -> List[str]:
    p = re.compile(regexp)
    return [f for f in children_files(path) if p.match(f) is not None]


def strip_prefix(sources: Iterable[str], prefix: str) -> List[str]:
    result = []
    prefix_length = len(prefix)
    for s in sources:
        if s.startswith(prefix):
            result.append(s[prefix_length:])
        else:
            result.append(s)
    return result


def get_package_data(base_dir: str, sub_dirs: Iterable[str]) -> List[str]:
    result = []
    for sub in sub_dirs:
        step0 = children_files(os.path.join(base_dir, sub))
        step1 = filter_ignore(step0, PACKAGE_DATA_IGNORE_PATTERNS)
        step2 = strip_prefix(step1, base_dir)
        step3 = strip_prefix(step2, "/")
        result += step3
    return result


def filter_match(source, patterns: Iterable[re.Pattern]) -> bool:
    for p in patterns:
        if p.match(source) is not None:
            return True
    return False


def default_version() -> str:
    return read_version(PACKAGE_INIT_PY)


def default_requirements() -> List[str]:
    return read_requirements(REQUIREMENTS)


def default_package_data() -> List[str]:
    return get_package_data(PACKAGE_DIR, PACKAGE_DATA_NAMES)


def default_packages() -> List[str]:
    return find_packages(where=SCRIPT_DIR, exclude=("test*",))


def default_compile_files() -> List[str]:
    all_python_files = match_files(path=PACKAGE_DIR, regexp=r".*\.py$")
    return filter_ignore(all_python_files, SPECIAL_DUNDER_FILE_PATTERNS)
