#!/bin/bash

basedir="$(dirname ${BASH_SOURCE[0]})/.."

python ${basedir}/integration-test.py -printcoords | python ${basedir}/scripts/update-integration-test-coordinates.py
