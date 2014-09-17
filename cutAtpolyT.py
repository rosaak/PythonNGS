#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
#  Copyright 2014 roshan padmanabhan <roshan@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  REQUIREMENTS none
#
#

'__version__' = 0.1
'__author__' = 'roshan padmanabhan'

'''
Purpose is to cut the sequences at polyT
get the two fragments and their length in a tab delimited format
if the seq is not cut it prints out the seq no and 'Not Found'
'''

import sys
import re

def usage():
    print('''
USAGE: cutAtpolyT.py infile.seq >out.tsv
    
	Purpose is to cut the sequences at polyT
	get the two fragments and their length in a tab delimited format
	if the seq is not cut it prints out the seq no and 'Not Found'    
    ''')

def openFile():
    try:
        inputFile = open(sys.argv[1],'r')
        return inputFile
    except Exception as e:
        print('\nOh No! => %s' %e)
        usage()
        sys.exit(2)

def cutLine(line,pX):
	'''
	function accepts two parameters
	first the line and the second regex compile
	'''
	for m in pX.finditer(line):
		#frag1= line[ : m.start()]
		#frag2= line[m.start():].rstrip()
		#fragmentinLine=[line.rstrip(),line[ : m.start()],line[m.start():].rstrip() ]
		fragmentinLine=[line.rstrip(),line[ : m.end()], line[m.end():].rstrip() ]
		if len(fragmentinLine) >=3	:
			#print len(fragmentinLine),
			return fragmentinLine
		

def cutLine2(line,pX):
	'''
	function accepts two parameters
	first the line and the second regex compile
	returns all the fragments as string
	>>>cutLine2(linepT)
	'['gtacgactagctac','acacacacaacacacaca']
	'''
	notFound=["Not Found"]
	fragments=[]
	try :
		for m in pX.finditer(line):
			frag1 = line[ : m.end()]
			frag2 = line[m.end():].rstrip()
			fragments =[ frag1 ,frag2]
			if len(frag2[2]) < 20:
				break
	except Exception as e:
		pass
	if len(fragments) >= 1:
		return fragments
	else :
		return notFound


def main():
	
	####### Open the File #######
	inf=openFile()
	
	####### compile some regex ######
	####### change here #########
	#pT1 = re.compile("T{5-9}G")
	pT = re.compile("TTTTTTTTTTTTG")
	pC = re.compile("TTTTTTTTTTTTC")
	
	####### print out header ########
	print "SeqNo\tFrag1\tlen_Frag1\tFrag2\tlen_Frag2"
	
	####### into the loop #######
	for index,line in  enumerate(inf.readlines()):
		try:
			####### change pT to some other compiled regex #########
			fragments = cutLine2(line,pT)
			if len(fragments) >1:
				print index,"\t", fragments[0],"\t",len(fragments[0]),"\t",fragments[1],"\t",len(fragments[1])
			elif len(fragments) == 1:
				print index,"\tNot_Found"
		except TypeError as e:
			pass	
	return 0

if __name__ == '__main__':
	main()

