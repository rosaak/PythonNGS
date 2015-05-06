import sqlite3
import argparse
import csv

__version__ = 0.1
__author__ = 'roshan padmanabhan'


'''
    input : pattern file, bedfile 
    pattern file :
        BC1 GTCCGATATGATTGCCGC
        BC2 ATGAGCCGGGTTCATCTT
        BC3 TGAGGCACTCTGTTGGGA
        BC4 ATGATTAGTCGCCATTCG
    bed file :
        chr2    227357721   227357812   +   ENSG00000168958 TGAAGGCATCTAAATGTG
        chr2    227356986   227357077   +   ENSG00000168958 TGAAGGCATCTAAATGTG
        chr7    98293279    98293355    -   ENSG00000006453 GACAGGCCATTTAACGTT
        chr20   56369400    56369491    -   ENSG00000087586 TACCAGTTCTAGATGTTA
        chr20   56383116    56384300    -   ENSG00000087586 TACCAGTTCTAGATGTTA
    outfiles :
        BC1.bed
        BC2.bed
        BC4.bed etc
    Aim :
        find the sequence in bed file and save the entire line as for example 
        BC1.bed , BC2.bed etc... 

'''

def read_bed_file(filename):
    """
    Return a list contains entire row from the bed file
    """
    outdata = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            outdata.append( row )
    return outdata


def split_bed_file(data):
    """
    Return the a list of tuple of two elements
    the entire row and the last element in the row
    """
    outdata = []
    for row in data:
        #outdata.append([row, ''.join(row.split("\t")[-1]) ])
        #print(row[-1])
        outdata.append( ( row, ''.join(row).split()[-1] ))
    return outdata


def create_db(datafilename=':memory:'):
    '''Return a db connction
    if no file name given then db is made in memory
    '''
    conn = sqlite3.connect(datafilename)
    return conn


def create_table(conn):
    '''
    Return conn
    caution : run this only once for a db
    '''
    conn.execute('''DROP TABLE IF EXISTS bedLines;''')
    conn.execute('''
        CREATE TABLE bedLines(
        complete_line text,
        sequence text 
        );
        ''')
    conn.commit()
    return conn.cursor()


def polpulate_table(tup):
    try:
        conn.execute("INSERT INTO bedLines (complete_line, sequence ) VALUES(?, ?)",( tup[0][0], tup[1]))
        conn.commit()
    except OperationalError as e:
        print (e)
        pass


def print_all():
    all_res = conn.execute('SELECT * FROM bedLines')
    return all_res


def query_db(pat):
    '''
    Returns the lines
    '''
    hdr = pat[0]
    query = pat[1].strip("\n")
    # TT = "GTCCGATATGATTGCCGC"
    # print(hdr,query,len(query))
    qres = conn.execute( 'SELECT complete_line FROM bedLines WHERE sequence= ? COLLATE NOCASE', [query] ).fetchall()
    #print(qres)
    fetched_lines=[]
    for i in qres:
        fetched_lines.append(i)
    # for i in fetched_lines:
    #     print(i[0])
    return fetched_lines

def save_file(list_of_lines, outfilename):
    with open(outfilename, 'w') as ofname:
        thewriter = csv.writer(ofname )
        thewriter.writerows(list_of_lines)


if __name__ == '__main__':

    des="""
    this script takes up a pattern file and data / bed file
    pattern file has two columns barcode id and the sequence  itself
    grepped lines will be saved into result files with the name as barcodeid.bed ex: BC1.bed etc
    """
    parser = argparse.ArgumentParser(description=des,formatter_class=argparse.RawTextHelpFormatter )
    parser.add_argument('-f', help='data file', action='store',dest='inBed',required=True)
    parser.add_argument('-p', help='pattern file', action='store',dest='pat_file',required=True)
    args = parser.parse_args()
    in_bed = args.inBed
    pat_file = args.pat_file

    # get the bed files into a list
    data = read_bed_file(in_bed)

    # making the database in memory and popluating the table
    conn=create_db()
    create_table(conn)

    # dynamically populate the table 
    for i in  split_bed_file(data):
        polpulate_table(i)

    # open the pattern file and search and save the files
    for each_pat in open(pat_file, 'r').readlines():
        q = each_pat.split("\t")
        results = query_db(q)
        # if there is results from the query then it is saved 
        if len(results) >=1 :
            final_bedfile = q[0]+'.bed'
            save_file(results, final_bedfile)
