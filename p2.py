import networkx as nx 
import matplotlib.pyplot as plt
import operator

G=nx.read_edgelist("anoncsv.csv",'rb',delimiter=',')

#PageRank
c=nx.pagerank(G)
sorted_c=sorted(c,key=operator.itemgetter(2))

#EigenVector Centrality
c=nx.eigenvector_centrality(G)
sorted_c=sorted(c,key=operator.itemgetter(2))

#Degree centrality

c=nx.degree_centrality(G)
sorted_c=sorted(c,key=operator.itemgetter(2))

#jaccard similarity
j=nx.jaccard_coefficient(G)


for u, v, p in j:
	print u, v, p
	print '\n'