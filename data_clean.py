import csv

usernames=[]
with open('idlist.tsv','r') as tsv:
	record=[line.strip().split('\t') for line in tsv]
i=0

temp=set()

for r in record:
	temp.add(r[0])
	temp.add(r[1])

usernames=list(temp)
print len(usernames)

"""for n in usernames:
	print "index",usernames.index(n)
	print "\t"
	print "item",n"""



f=open('anonlist.tsv','a')

for r in record:
	f.write(str(usernames.index(r[0])))
	f.write('\t')
	f.write(str(usernames.index(r[1])))
	f.write('\n')


f.close()





	