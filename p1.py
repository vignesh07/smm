import networkx as nx 
import matplotlib.pyplot as plt

G=nx.read_edgelist("anoncsv.csv",'rb',delimiter=',')

"""count=0
tri=nx.triangles(G)
x=tri.values()

for xx in x:
	print xx
	count=count+int(xx)

print count
"""
"""i=1
count=0
while(i<1001):
	count = count + tri[i]
	print count
	i=i+1

print "count", count"""
"""degree_sequence=sorted(nx.degree(G).values(),reverse=True) 
dmax=max(degree_sequence)
plt.loglog(degree_sequence,'b-',marker='o')
print dmax
plt.savefig('degree_dist.png')
plt.show()"""
""""g=nx.DiGraph(G)
count=0
for n in nx.simple_cycles(g):
	print list(n)
	if len(list(n))==3:
		print list(n)
		count=count+1
		print count

print count"""


d=nx.diameter(G)


print "\n diameter", d