#!/usr/bin/env bash

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" || exit; pwd)

read -r -p "Please enter a daemon name: reccd-" DAEMON_NAME

FULLNAME_INIT_FILES=(
    "$ROOT_DIR/black.sh"
    "$ROOT_DIR/flake8.sh"
    "$ROOT_DIR/isort.cfg"
    "$ROOT_DIR/isort.sh"
    "$ROOT_DIR/mypy.sh"
    "$ROOT_DIR/pytest.ini"
    "$ROOT_DIR/README.md"
    "$ROOT_DIR/setup.cfg"
    "$ROOT_DIR/uninstall.sh"
)

for f in ${FULLNAME_INIT_FILES[*]}; do
    sed -i.tmp -e "s/reccd\([\._-]\)template/reccd\\1$DAEMON_NAME/g" "$f"
done

mv -v "$ROOT_DIR/reccd_template" "$ROOT_DIR/reccd_$DAEMON_NAME"

echo "Remove all *.tmp files ..."
find . -name '*.tmp' -exec rm -v {} \;

read -r -p "Remove init.sh file? (y/n) " YN
if [[ $YN == 'y' || $YN == 'Y' ]]; then
    rm -v "$ROOT_DIR/init.sh"
fi
