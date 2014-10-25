import csv

ff=open('mapping.tsv','a')
fff=open('anon.tsv','a')



with open('sampled.tsv','r') as tsv:
	record=[line.strip().split('\t') for line in tsv]


mapping=dict()
names=set()
i=0

for r in record:
	if r[0] not in names:
		i=i+1
		mapping.update({r[0]:i})
		ff.write(str(r[0]))
		ff.write('\t')
		ff.write(str(mapping[r[0]]))
		ff.write('\n')
		names.add(r[0])
	if r[1] not in names:
		i=i+1
		mapping.update({r[1]:i})
		ff.write(str(r[1]))
		ff.write('\t')
		ff.write(str(mapping[r[1]]))
		ff.write('\n')
		names.add(r[1])

for r in record:
	fff.write(str(mapping[r[0]]))
	fff.write('\t')
	fff.write(str(mapping[r[1]]))
	fff.write('\n')


ff.close()
fff.close()



