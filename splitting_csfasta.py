from Bio import SeqIO
import os
import sys
'''
This scrtpt slice the fasta sequence at a fixed position and gives the first half
'''
def openFile():
	try:
		inputFile = open(sys.argv[1], 'r')
		return inputFile
	except Exception as e:
		print('\nOh No! => %s ' %e)
		print('\nUSAGE:splitting_csfasta.py infile.csfasta number_to_cut\n')
		sys.exit(2)

def main():
	number=int(sys.argv[2])
	infile = openFile()
	#print infile.name
	for index, record in enumerate(SeqIO.parse(infile.name,"fasta")):
		each_id = record.id
		each_seq = record.seq
		each_length = len(record.seq)
		print ">%s\n%s"  %(each_id,each_seq[number:]) #change here
if __name__ == '__main__':
	main()
