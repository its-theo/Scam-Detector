#!/bin/sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
poetry new dependencies
poetry add nextcord
poetry add pyjavaproperties
poetry install
python3 bot.py
