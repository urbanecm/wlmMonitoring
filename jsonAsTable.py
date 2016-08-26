#!/bin/bash
#-*- coding: utf-8 -*-

import json
f = open('output.json', 'r')
data = json.loads(f.read())

print '{|class="wikitable sortable"'
print '!Seznam památek !! Památek !! Souřadnice !!  %  !! Článek !! % !! Obrázek !! % !! Commonscat !! %'
for monument in data:
	print '|-'
	print '| [[' + monument + ']] || ' + str(data[monument]['total']) + ' || ' + str(data[monument]['coor']) + ' || ' + float(data[monument]['coor']/(float(data[monument]['total'])/float(100)) + ' || ' + str(data[monument]['article']) + ' || ' + float(data[monument]['article']/(float(data[monument]['total'])/float(100)) + ' || ' + str(data[monument]['image']) + ' || ' + float(data[monument]['image']/(float(data[monument]['total'])/float(100)) + ' || ' + str(data[monument]['commonscat']) + ' || ' + data[monument]['commonscat']/(float(data[monument]['total'])/float(100))

print '|-class="sortbottom"'
print '|}'
