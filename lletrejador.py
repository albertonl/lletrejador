	#!/usr/bin/env/python
# -*- coding: utf-8 -*-

# Lletrejador de català
# Alberto Navalon Lillo (C) May 2019
# This software is subject to the GNU General Public License
# For further information and details, visit the repository page:
# https://github.com/albertonl/lletrejador

from xml.dom import minidom # To parse the document
import subprocess as sp # Subprocesses
import random # To use the random.randint() function to generate a random index to give a word

# We parse all elements in Catalan dictionary
xmldoc = minidom.parse('apertium-cat.cat.dix')
elist = xmldoc.getElementsByTagName('e')

dicts = []
for e in elist:
	d = {}
	for a in e.attributes.values():
		d[a.name] = a.value
	dicts.append(d)



finished = False
answer = 's'
# Main loop
while finished==False:
	sp.call('clear',shell=True)
	ran_num = random.randint(0,len(dicts)-1)
	if 'lm' in dicts[ran_num].keys():
		word = dicts[ran_num]['lm']
	else:
		continue
	print(word)	
	print("\n")
	word = word.lower()
	for i in range(0,len(word)):
		if word[i]==' ':
			print(" ", end=" ")
		elif word[i]=='a':
			print("a", end=" ")
		elif word[i]=='b':
			print("be", end=" ")
		elif word[i]=='c':
			print("ce", end=" ")
		elif word[i]=='d':
			print("de", end=" ")
		elif word[i]=='e':
			print("e", end=" ")
		elif word[i]=='f':
			print("efe", end=" ")
		elif word[i]=='g':
			print("ge", end=" ")
		elif word[i]=='h':
			print("hac", end=" ")
		elif word[i]=='i':
			print("i", end=" ")
		elif word[i]=='j':
			print("jota", end=" ")
		elif word[i]=='k':
			print("ca", end=" ")
		elif word[i]=='l':
			if word[i+1]=='·' and word[i+2]=='l' and i<(len(word)-2): # it could give a 'string index out of range' error
				print("ele geminada", end=" ")
			else:
				print("ele", end=" ")
		elif word[i]=='m':
			print("eme", end=" ")
		elif word[i]=='n':
			print("ene", end=" ")
		elif word[i]=='o':
			print("o", end=" ")
		elif word[i]=='p':
			print("pe", end=" ")
		elif word[i]=='q':
			print("cu", end=" ")
		elif word[i]=='r':
			print("erre", end=" ")
		elif word[i]=='s':
			print("esse", end=" ")
		elif word[i]=='t':
			print("te", end=" ")
		elif word[i]=='u':
			print("u", end=" ")
		elif word[i]=='v':
			print("ve (baixa)", end=" ")
		elif word[i]=='w':
			print("ve doble", end=" ")
		elif word[i]=='x':
			print("ics", end=" ")
		elif word[i]=='y':
			print("i grega", end=" ")
		elif word[i]=='z':
			print("zeta", end=" ")
		else:
			print("??", end=" ")
		
		if i<(len(word)-1):
			print("-", end=" ")
	
	print("\n")
	answer = input("Vols continuar? (s/n): ")
	if answer=='n':
		finished = True
		quit()
