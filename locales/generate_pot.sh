#!/usr/bin/env bash
pybabel extract -o messages.pot ../cogs ../utils
# xgettext --language=Python --add-comments=TRANSLATORS: --force-po -o ./messages.pot ../**/*.py

pybabel init -l en -i ./messages.pot -d ./
pybabel compile -d ./
