#coding:gbk
'''
程序目标：
程序作者：郭杰
'''


import jieba,os,sys,codecs,math
import jieba.posseg as pseg


names = {}
relationships = {}
linenames = []

jieba.load_userdict('name.txt')
with codecs.open('黎明破晓的街道.txt','r') as f:
	for line in f.readlines():
		poss = pseg.cut(line)
		linenames.append([])
		for w in poss:
			if w.flag != 'nr' or len(w.word) < 2:
				continue
			linenames[-1].append(w.word)
			if names.get(w.word) is None:
				names[w.word] = 0
				relationships[w.word] = {}
			names[w.word] += 1

for line in linenames:
	for name1 in line:
		for name2 in line:
			if name1 == name2:
				continue
			if relationships[name1].get(name2) is None:
				relationships[name1][name2] = 1
			else:
				relationships[name1][name2] = relationships[name1][name2] + 1
				
with codecs.open('node.txt','w','gbk') as f:
	f.write('Id Label Weight\r\n')
	for name, times in names.items():
		f.write(name + ' ' + name + ' ' + str(times) + '\r\n')

with codecs.open('edge.txt','w','gbk') as f:
	f.write('Source Target Weight\r\n')
	for name, edges in relationships.items():
		for v, w in edges.items():
			if w > 3:
				f.write(name + ' ' + v + ' ' + str(w) + '\r\n')
