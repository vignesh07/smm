import networkx as nx 
import matplotlib.pyplot as plt
import operator

G=nx.read_edgelist("anoncsv.csv",'rb',delimiter=',')


degree_sequence=sorted(nx.degree(G).values(),reverse=True) # degree sequence
#print "Degree sequence", degree_sequence
dmax=max(degree_sequence)

plt.loglog(degree_sequence,'b-',marker='o')
plt.title("Degree rank plot")
plt.ylabel("degree")
plt.xlabel("rank")

plt.savefig("degree_histogram.png")

count=0
tri=nx.triangles(G)
x=tri.values()

for xx in x:
	print xx
	count=count+int(xx)

print count

T=nx.minimum_spanning_tree(G,weight='weight')
print T.edges(data=True)

##print ccc-sss