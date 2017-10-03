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
	
	count_sequences=0
	for line in FASTA:
		if line.startswith('>'):
			count_sequences+=1
		else:
			line = line.strip()
			while len(line)>=4:
				word=line[0:4]
				if not word in count_dict:
					count_dict[word]=count
				else:
					count_dict[word]+= 1
				line=line[1:]
	print "total number of sequences = %d" %(count_sequences)


	#for key, value in sorted(count_dict.iteritems(), key=lambda (k,v): (v,k)):
    		#print "%s: %s" % (key, value)
	top_scoring_tetra = sorted(count_dict, key=lambda key: count_dict[key], reverse=True)[:16]
	print top_scoring_tetra

	count_sequences=0
	count_sequence_presence=0
	dict_fraction = {}
	for tetra in top_scoring_tetra:
		dict_fraction[tetra]=count_sequence_presence
		for sequence in FASTA:			
			if sequence.startswith('>'):
				pass
			else:
				sequence=sequence.strip()
				if tetra in sequence:
					dict_fraction[tetra]+=1

	for key, value in dict_fraction.items():
		print "%s occurs in %s number of sequences" %(key, value)

		



if __name__=="__main__":
    createParser()
    main(sys.argv[1:])





  
 







