#!/bin/bash

rm output.json
rm mediawiki.mw
./wlmMonitoring.py
./jsonAsWikitable.sh
echo "Current results are in mediawiki.mw in wikitable and in output.json in JSON
