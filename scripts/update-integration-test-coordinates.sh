#!/bin/bash

basedir="$(dirname ${BASH_SOURCE[0]})/.."

cd $basedir

python integration-test/__init__.py --print-coords | python scripts/update-integration-test-coordinates.py
