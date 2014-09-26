#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SequenceStatistics.py
#
# Copyright 2012 roshan padmanabhan <rosaak@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# Aim : Calculate the Statistics of each sequence for from a
# multifasta file.
#
# Require Biopython.

#print "Usage : python SequenceStatistics.py absolute_path_of_fasta_file > OutfileName "

__version__ = 0.1
__author__ = 'Roshan'
__name__ ='SequenceStatistics.py'

import sys
FileName = sys.argv[1]
try :
    print("SeqName\tSeqlen\tGC%\tCountA\tCountT\tCountG\tCountC\tCountN\tCountR\tCountY\tCountM\tCountK\tCountS\tCountW\tCountB\tCountD\tCountH\tCountV\tCountG+C\tCountA+T")
    from Bio import SeqIO
    for seq_record in SeqIO.parse(FileName, "fasta"): # CHANGE THE FILE INPUT HERE
    	seq_record.upper()
	CountA = seq_record.seq.count("A")
	CountT= seq_record.seq.count("T")
	CountG= seq_record.seq.count("G")
	CountC= seq_record.seq.count("C")
	CountN= seq_record.seq.count("N")
	CountR= seq_record.seq.count("R")
	CountY= seq_record.seq.count("Y")
	CountM= seq_record.seq.count("M")
	CountK= seq_record.seq.count("K")
	CountS= seq_record.seq.count("S")
	CountW= seq_record.seq.count("W")
	CountB= seq_record.seq.count("B")
	CountD= seq_record.seq.count("D")
	CountH= seq_record.seq.count("H")
	CountV= seq_record.seq.count("V")
	CountGplusC= seq_record.seq.count("G")+seq_record.seq.count("C")
	CountAplusT= seq_record.seq.count("A")+ seq_record.seq.count("T")
	SeqLen=len(seq_record)
	pGC=((CountGplusC)*100/(SeqLen))
	print (seq_record.id,SeqLen,pGC,CountA,CountT,CountG,CountC,CountN,CountR,CountY,CountM,CountK,CountS,CountW,CountB,CountD,CountH,CountV,CountGplusC,CountAplusT,"\n") #,"\t",seq_record.seq
except:
    pass
def main():
    return 0

if __name__ == '__main__':
	main()


