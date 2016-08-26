#!/bin/bash

wget -O input.csv https://json-csv.com/?u=http://tools.wmflabs.org/urbanecmbot/test/wlmMonitoringOutput.json
./csvToMw.pl
rm input.csv
