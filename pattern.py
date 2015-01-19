"""
Copyright [2014] [roshan padmanabhan]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
'''

	 input : pattern file, bedfile 
	 gives the highest val from bedfile

'''
import math

def getmaxvalue(l):
	r={}
	for e, i in enumerate(l):
		r[e]=int((i.strip().split(',')[1].split('\t')[1]))
	#print (r)
	for i in r.items() :
		#print (max(r.values()))
		if i[1] == max(r.values()):
			res= l[i[0]]
	return res.strip('\n')

with open('MOB.bed','r') as fh:
	data=fh.readlines()
	
# making three dictionaries using bed file whcih has to be quiried
# dp1 and dp2 for start and end pattern where key is start or end position and value is the line number strating from 0
# dictionary dl hold each line as key and value as line number 
dp1 = {} 
#dp2 = {}
dl  = {}

# populating dictionary
for e,line in  enumerate(data[:]):
	dp1[(line.split()[0],line.split()[1])] = e
	#dp2[(line.split()[0],line.split()[2])] = e   
	dl[e]=line

# read the pattern file
with open('../data/par_30_2_100.bed','r') as fh:
	pats=fh.readlines()


for e in pats[:]:
	try:
		# lines in patternfiles are split took start_pattern and end_pattern
		p1= (''.join(e.split()[0]) ,''.join(e.split()[1]) )
		p2= (''.join(e.split()[0]) ,''.join(e.split()[2]) )
		# seach   in dictionaies and the return values are line numbers
		# for those range of line numbers
		# pull the  lines and get the line with max value
		matched_lines=[]
		for i in  (range(int(dp1[p1]),int(dp1[p2]))):
			matched_lines.append(dl[i])
			getmaxvalue(matched_lines)
		print (p1[1],p2[1],getmaxvalue(matched_lines))

	except KeyError as e:
		#print( e )
		#print (p1[1],p2[1])   # uncomment the line if you want to know which are the one not found in the MOB file
		pass
		
