#!/usr/bin/env bash

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" || exit; pwd)

"$ROOT_DIR/python" -m mypy \
    --config-file="${ROOT_DIR}/mypy.ini" \
    "$ROOT_DIR/setup.cython.py" \
    "$ROOT_DIR/setup.py" \
    "$ROOT_DIR/setup_utils.py" \
    "$ROOT_DIR/setup_variables.py" \
    "$ROOT_DIR/answer_daemon_template/" \
    "$ROOT_DIR/tester/" \
    "$ROOT_DIR/test/"
