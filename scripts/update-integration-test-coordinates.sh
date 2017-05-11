#!/bin/bash
python integration-test.py -printcoords | python scripts/update-integration-test-coordinates.py
