#!/usr/bin/env bash

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" || exit; pwd)

"$ROOT_DIR/python" setup.cython.py bdist_wheel

echo "Remove all '*.c' files ..."
find "$ROOT_DIR/answer_daemon_template" -name "*.c" -exec rm -v '{}' \;
