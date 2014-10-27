import csv




ff=open('anoncsv.csv','a')
with open('anon.tsv','r') as tsv:
	record=[line.strip().split('\t') for line in tsv]

for r in record:
	ff.write(str(r[0]))
	ff.write(',')
	ff.write(str(r[1]))
	ff.write('\n')



ff.close()