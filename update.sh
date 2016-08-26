#!/bin/bash

rm -f output.json mediawiki.mw warnings.json
./wlmMonitoring.py
./jsonAsWikitable.sh
echo "Current results are in mediawiki.mw in wikitable and in output.json in JSON
