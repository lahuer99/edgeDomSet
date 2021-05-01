# networkx is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and function of complex networks(like graphs!).
import networkx as nx
from itertools import chain, combinations

# import kernelization
# input graph in question
G=nx.Graph()

#parameter[if there is a k-eds?] 
k=5

# max size possible for vc [p<0 => NO instance]
p=2*k

# adding vertices of graph
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
# G.add_node(4)
# G.add_node(5)
# G.add_node(6)
# G.add_node(7)

# adding edges of graph
G.add_edge(0,1)
# G.add_edge(0,7);
# G.add_edge(6,7);
G.add_edge(1,2);
G.add_edge(2,3);
G.add_edge(3,0);
# G.add_edge(2,4);
# G.add_edge(4,5);
# G.add_edge(5,6);

vertices=list(G.nodes)
edges=list(G.edges)

# print(list(nx.connected_components(G)))

# try:
# 	print(list(nx.find_cycle(G)))
# except:
# 	print(list(nx.cycle_basis(G)))
# 	print("no c")

# print(sorted(G.degree,key=lambda x:x[1],reverse=True)[0])

# check starting branching with each vertex recursively
C=I=U1=[]
U2=vertices

print(sorted(G.degree,key=lambda x:x[1],reverse=True))

# print([x[0] for x in sorted(G.degree,key=lambda x:x[1],reverse=True) if x[1]>=3])
def powerset(iterable,z):
	s=list(iterable)
	return chain.from_iterable(combinations(s,r) for r in range(1,z+1))

P=[{0, 1, 2}, {3, 4, 5},{6,7,8}]

y=len(P)
	# if y>min(p1,k):
		# print("mm")
		# return
p1=5
z=min(p1-y,k-y)
print(z)
Psubs=list(powerset(P,z))
print("Psubs")
print(Psubs)


Gcopy=G.copy()
Gdash=G.copy()

CC=[2,7,4,6]
UU=[[0,1],[3]]
Gcopy.remove_nodes_from([i for i in vertices + CC if i not in vertices or i not in CC])


toremove=list(nx.maximal_matching(Gcopy))
print(toremove)

k1=k
eds=[]
