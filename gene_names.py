#!/usr/bin/python
import fileinput
import re

fileinput.close( )

count = 0
total = [ ]
for line in fileinput.input('/home/xianghui/data/Homo_sapiens.GRCh37.75.gtf'):

    if line.strip()[0] != '#':
	dic = {}
	splitted = line.split('\t')
	dic['geneName'] = re.findall('gene_name \"(.*?)\";',splitted[8])[0]
	dic['chr'] = splitted[0]
	dic['startPos'] = splitted[3]
	dic['endPos'] = splitted[4]
	total.append(dic)

fileinput.close( )

print (total)
