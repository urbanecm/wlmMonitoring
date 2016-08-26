#!/bin/bash

cp output.json /data/project/urbanecmbot/test/wlmMonitoringOutput.json
wget -O input.csv https://json-csv.com/?u=http://tools.wmflabs.org/urbanecmbot/test/wlmMonitoringOutput.json &> /dev/null
./csvToMw.pl
rm input.csv
