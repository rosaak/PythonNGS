#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  removeEmptyLinesFromFastq.py
#  
#  Copyright 2014 roshan padmanabhan <rosaak@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  See the GNU General Public License for more details.
#  WITHOUT ANY WARRANTY
#

__version__ = 0.1
__author__ = 'roshan padmanabhan'

'''
it might work with python 2

what it does is to open the fastq file as list and reads makes a dictionary of 
  line number and first three character as key value pair

the main function finds out the empty lines from the dictionary 
  and creates a list of index of lines (empty line and above line)

this list is used to remove the lines from the initial file 
  open a new file in write mode and save the new list of lines

'''

import sys
import re

def usage():
    print('''
USAGE: python3 removeEmptyLinesFromFastq.py infile.fastq newfile.fastq
    
	Purpose: remove empty lines from fastq
	
	Caution:This is a rudimentary script
	So if any other file type is given
	it may give unexpected results
	
    ''')

def openFile():
    try:
        inputFile = open(sys.argv[1],'r')
        return inputFile
    except Exception as e:
        #print('\nOh No! => %s' %e)
        usage()
        sys.exit(2)



def makedict(fileAsList):
	'''
	key is line number
	value is the first three char of each line
	if line is empty give value as '***' whcih is unlikely in fastq
	'''
	dict={}
	for e , line in enumerate(fileAsList):
		f3 = line[0:3]
		if re.match('^\n',f3) :
			dict[e] = '***' ###this is just to visually 
		else :
			dict[e] = line[0:3]
	return dict

def main():
	# open file
	fq = openFile().readlines() 
	
	# making dict 
	d = makedict(fq)	
	
	# new dict
	r2d2 = {key: value for (key, value) in d.items() if value == '***'}		
	
	# here I got the empty lines
	emptyLine = list(r2d2.keys())
	print("EmptyLines : ", emptyLine)
	
	# get the above line
	linesAbove = [ element-1 for element in emptyLine]
	print("Lines Above : ",linesAbove)
	
	# lines to remove
	linesToRemove = linesAbove + emptyLine
	linesToRemove.sort()
	print("Lines to remove : ", linesToRemove)
	
	# remving the lines from fq and making a new list called nfq
	nfq = [i for j, i in enumerate(fq) if j not in linesToRemove]
	
	# write to a new file
	# change this
	wfname = "newfastq"  
	#wfname = sys.argv[2]  # if a name is not given it will give error , have to modify later
	
	with open(wfname, "wt") as out_file:
		out_file.write(''.join(str(line) for line in nfq))
	out_file.close()
	print ("check file --->", wfname)
	print ("...............Over and Out...............")
	
if __name__ == '__main__':
	main()

