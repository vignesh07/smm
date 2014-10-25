import csv



f=open('idlist.tsv','r')

with open('idlist.tsv','r') as tsv:
	record=[line.strip().split('\t') for line in tsv]

print len(record)
f.close()

t=open('sampled.tsv','a')

count=0
prev=str(record[0][0])
print prev
done=[]
for r in record:
	if(prev!=str(r[0])):
		count=0
		done.append(prev)
	if(count>999):
		done.append(r[0])
		continue
	prev=str(r[0])
	count=count+1
	if r[0] in done: continue
	t.write(str(r[0]))
	t.write('\t')
	t.write(str(r[1]))
	t.write('\n')



t.close()



	
