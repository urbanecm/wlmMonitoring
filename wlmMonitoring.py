#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Import libs and init them
import urllib
import json
from wmflabs import db
connHeritage = db.connect('s51138__heritage_p')
connWiki = db.connect('cswiki')

warnings = []

#Get all monuments lists in cswiki
cur = connWiki.cursor()
with cur:
	sql = 'select page_title from page where page_namespace=0 and page_is_redirect=0 and page_id in (select tl_from from templatelinks where tl_title="Památky_v_Česku");'
	cur.execute(sql)
	lists = cur.fetchall()

res = {}
for row in lists:
	totalZero = False
	#For every list fetch required data
	rowData = {}
	monumentListEncoded = urllib.quote_plus(row[0])
	monumentList = row[0]
	#Get num of monuments in the list
	cur = connHeritage.cursor()
	with cur:
		sql = 'select count(*) from `monuments_cz_(cs)` where source like "//cs.wikipedia.org/w/index.php?title=' + monumentListEncoded + '&oldid=%";'
		cur.execute(sql)
		data = cur.fetchall()
	rowData['total'] = data[0][0]
	if rowData['total'] == 0:
		totalZero = True
		warnings.append("Total is zero in list named " + monumentList)
	#Get num of monuments with an image in the list
	cur = connHeritage.cursor()
	with cur:
		sql = 'select count(*) from `monuments_cz_(cs)` where source like "//cs.wikipedia.org/w/index.php?title=' + monumentListEncoded + '&oldid=%" and image!="";'
		cur.execute(sql)
		data = cur.fetchall()
	rowData['image'] = data[0][0]
	if totalZero == False:
		rowData['image%'] = float(rowData['image'])/(float(rowData['total'])/float(100))
	else:
		rowData['image%'] = 0
	#Get num of monuments with an article in the list
	cur = connHeritage.cursor()
	with cur:
		sql = 'select count(*) from `monuments_cz_(cs)` where source like "//cs.wikipedia.org/w/index.php?title=' + monumentListEncoded + '&oldid=%" and monument_article!="";'
		cur.execute(sql)
		data = cur.fetchall()
	rowData['article'] = data[0][0]
	if totalZero == False:
		rowData['article%'] = float(rowData['article'])/(float(rowData['total'])/float(100))
	else:
		rowData['article%'] = 0
	#Get num of monuments with lon+lat in the list
	cur = connHeritage.cursor()
	with cur:
		sql = 'select count(*) from `monuments_cz_(cs)` where lat is not null and lon is not null and source like "//cs.wikipedia.org/w/index.php?title=' + monumentListEncoded + '&oldid=%";'
		cur.execute(sql)
		data = cur.fetchall()
	rowData['coor'] = data[0][0]
	if totalZero == False:
		rowData['coor%'] = float(rowData['coor'])/(float(rowData['total'])/float(100))
	else:
		rowData['coor%'] = 0
	#Get num of monuments with commonscat in the list
	cur = connHeritage.cursor()
	with cur:
		sql = 'select count(*) from `monuments_cz_(cs)` where source like "//cs.wikipedia.org/w/index.php?title=' + monumentListEncoded +'&oldid=%" and commonscat!="";'
		cur.execute(sql)
		data = cur.fetchall()
	rowData['commonscat'] = data[0][0]
	if totalZero == False:
		rowData['comonscat%'] = float(rowData['commonscat'])/(float(rowData['total'])/float(100))
	else:
		rowData['commonscat%'] = 0
	#Add rowData to all results
	res[monumentList] = rowData

#Data to JSON
of = open('output.json', 'w')
of.write(json.dumps(res))
#Warnings to JSON
wf = open('warnings.json', 'w')
wf.write(json.dumps(warnings))
