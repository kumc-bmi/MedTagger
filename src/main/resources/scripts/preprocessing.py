import sys
import csv
import os.path

def main(args):
	counter = 0
	path_to_input = args[0]
	fmap = open(os.path.join(path_to_input, 'mapping_ids_pat.csv'),'w')
	with open(os.path.join(path_to_input,'notes.csv')) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for i in readCSV:
			f=open(os.path.join(path_to_input,str(counter)+".txt"),"w")
			if i[2] == 'NOTE_TEXT':
				continue
			f.write(i[2])
			fmap.write(i[1]+','+i[16]+','+str(counter)+'\n') #(NOTE_ID, PAT_MRN)
			counter=counter+1
			f.close()
	fmap.close()

if __name__ == "__main__":
    main(sys.argv[1:])
