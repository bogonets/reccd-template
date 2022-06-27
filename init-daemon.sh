#!/usr/bin/env bash

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" || exit; pwd)

read -r -p "Please enter a daemon name: answer-daemon-" DAEMON_NAME

FULLNAME_INIT_FILES=(
  "$ROOT_DIR/black.sh"
  "$ROOT_DIR/build.cython.sh"
  "$ROOT_DIR/clean.sh"
  "$ROOT_DIR/flake8.sh"
  "$ROOT_DIR/isort.cfg"
  "$ROOT_DIR/isort.sh"
  "$ROOT_DIR/mypy.sh"
  "$ROOT_DIR/pytest.ini"
  "$ROOT_DIR/README.md"
  "$ROOT_DIR/setup_variables.py"
  "$ROOT_DIR/uninstall.sh"
  "$ROOT_DIR/upgrade.sh"
  "$ROOT_DIR/answer_daemon_template/__init__.py"
  "$ROOT_DIR/answer_daemon_template/daemon/singleton_daemon.py"
  "$ROOT_DIR/test/daemon/test_singleton_daemon.py"
)

for f in ${FULLNAME_INIT_FILES[*]}; do
  sed -i.tmp -e "s/answer\([\._-]\)daemon\([\._-]\)template/answer\\1daemon\\2$DAEMON_NAME/g" "$f"
done

mv -v "$ROOT_DIR/answer_daemon_template" "$ROOT_DIR/answer_daemon_$DAEMON_NAME"

echo "Remove all *.tmp files ..."
find . -name '*.tmp' -exec rm -v {} \;

read -r -p "Remove init-daemon.sh file? (y/n) " YN
if [[ $YN == 'y' || $YN == 'Y' ]]; then
  rm -v "$ROOT_DIR/init-daemon.sh"
fi
