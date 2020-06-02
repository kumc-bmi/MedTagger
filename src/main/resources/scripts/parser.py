import sys
import csv
import os.path

def map_patients(path_to_input):
	mapDc = {}
	f = open(os.path.join(path_to_input, "mapping_ids_pat.csv") , "r")
	f = f.readlines()
	for i in f:
		i = i.rsplit('\n')[0]
		i = i.rsplit(',')
		mapDc[i[2]] = [i[0],i[1]]
	#print (mapDc)
	return mapDc

def main(args):
	path_to_input = args[0]
	path_to_output = args[1]
	counter = 0
	import glob
	files = (glob.glob(os.path.join(path_to_output,'*.ann')))
	print (os.path.join(path_to_output,'*.ann'))
	output = open(os.path.join(path_to_output,'observation_fact_covid_symptoms.csv'),'w')
	for f in files:
		counter=counter+1
		readf = open(f,"r")
		line = (readf.read()).rsplit('\n')
		fstline = True
		for l in line:
			terms = l.rsplit('\t')
			if len(terms)<10:
				continue
			if fstline:
				mapDc = map_patients(path_to_input)
				print (terms[0][:-4])
				filename = mapDc[terms[0][:-4]]
				fstline = False
			#print (terms[0])
			certainty = terms[6]
			certainty =  certainty[certainty.index('"')+1:certainty.rindex('"')]
			status = terms[7]
			status =  status[status.index('"')+1:status.rindex('"')]
			experiencer = terms[8]
			experiencer =  experiencer[experiencer.index('"')+1:experiencer.rindex('"')]
			concept = terms[9]
			concept =  concept[concept.index('"')+1:concept.rindex('"')]
			#print (filename)
			output.write(filename[0]+','+filename[1]+','+terms[0]+','+ concept +','+ status +','+ experiencer +','+ certainty +"\n")
			#(NOTE_ID, PAT_MRN, filename, concept, status, experiencer, certainty)
	output.close()
	
if __name__ == "__main__":
    main(sys.argv[1:])
