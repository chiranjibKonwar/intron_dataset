from optparse import OptionParser
import sys, re
from itertools import product
usage= sys.argv[0] + """ -f FASTA_intron_sequence_file"""

parser = None
def createParser():
	global parser
	epilog = """
     This code takes input a FASTA intron sequence and computes overall tetranucleotide frequency for the input intron sequences"""

	epilog = re.sub(r'[ \t\f\v]+',' ', epilog)

    	parser = OptionParser(usage=usage, epilog=epilog)

    	parser.add_option("-f", "--input_file_intron_sequences", dest="input_file",
                      help='the input intron sequence fasta file [REQUIRED]')

def main(argv, errorlogger = None, runstatslogger = None):
	global parser
	(opts, args) = parser.parse_args(argv)
	filename=opts.input_file   	
	fh=open(filename,'r')
	FASTA=fh.readlines()	

	count_dict = {}
	count =1
	for possible_word in product('ATCG', repeat=4):
    		count_dict["".join(possible_word)] = 0

        t = 0
	for line in FASTA:
		if line.startswith('>'):
			pass
		else:
			line = line.strip()
			while len(line)>=4:
				word=line[0:4]
				if not word in count_dict:
					count_dict[word]=count
				else:
					count_dict[word]+= 1
				line=line[1:]
				t+=1

	print t
	for k,v in count_dict.items():
		print k, float(v)/float(t)*100




if __name__=="__main__":
    createParser()
    main(sys.argv[1:])





  
 







