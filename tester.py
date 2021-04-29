# networkx is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and function of complex networks(like graphs!).
import networkx as nx
from itertools import chain, combinations

# import kernelization
# input graph in question
G=nx.Graph()

#parameter[if there is a k-eds?] 
k=3

# max size possible for vc [p<0 => NO instance]
p=2*k

# adding vertices of graph
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)

# adding edges of graph
G.add_edge(0,1)
G.add_edge(0,7);
G.add_edge(6,7);
G.add_edge(1,2);
G.add_edge(2,3);
G.add_edge(3,4);
G.add_edge(2,4);
G.add_edge(4,5);
G.add_edge(5,6);

vertices=list(G.nodes)
edges=list(G.edges)

# print(sorted(G.degree,key=lambda x:x[1],reverse=True)[0])

# check starting branching with each vertex recursively
C=I=U1=[]
U2=vertices

# print(sorted(G.degree,key=lambda x:x[1],reverse=True))

# print([x[0] for x in sorted(G.degree,key=lambda x:x[1],reverse=True) if x[1]>=3])

Gcopy=G.copy()
Gdash=G.copy()

CC=[2,7,4,6]
UU=[[0,1],[3]]
Gcopy.remove_nodes_from([i for i in vertices + CC if i not in vertices or i not in CC])


toremove=list(nx.maximal_matching(Gcopy))
print(toremove)

def theenumerator(GG,CC,II,UU):
	# < need to deal with II>
	Gdash=G.copy()
	k1=k
	eds=[]
	print(CC)
	Gcopy=G.copy()
	Gcopy.remove_nodes_from([i for i in vertices + CC if i not in vertices or i not in CC])

	# print(II)
	# Gdash.remove_nodes_from(II)
	# Gcopy.remove_nodes_from(II)

	toremove=list(nx.maximal_matching(Gcopy))
	UU1=list(UU)

	for u,v in toremove:
		if u in list(Gdash.nodes):
			Gdash.remove_node(u)
		if v in list(Gdash.nodes):
			Gdash.remove_node(v)
		if u in CC:
			CC.remove(u)
		if v in CC:
			CC.remove(v)

		k1-=1
		eds.append((u,v))
		if k1<=0 and len(list(Gdash.edges))==0:
			# print(eds)
			theds.append(eds)
			return	
	
	if k1-len(list(Gdash.edges))>=0:
		eds.extend(list(Gdash.edges))
		# print(eds)
		theds.append(eds)
		return


	for ve in CC:
		k1-=1

		nlist=sorted([(G.degree(x),x) for x in [n for n in G.neighbors(ve)]],key=lambda y:y[0],reverse=True)
		for d,chve in nlist:
			rem_enum(ve,chve,eds,Gdash,CC)

		# eds.append((ve,chve))
		# if ve in list(Gdash.nodes):
		# 	Gdash.remove_node(ve)
		# if chve in list(Gdash.nodes):
		# 	Gdash.remove_node(chve)

		# if ve in CC:
		# 	CC.remove(ve)
		# if chve in CC:
		# 	CC.remove(chve)
		# if k1<=0 and len(list(Gdash.edges))==0:
		# 	theds.append(eds)
		# 	return	


def rem_enum(eds,Gdash,CC,k1):
	for ve in CC:
		for d,chve in sorted([(G.degree(x),x) for x in [n for n in G.neighbors(ve)]],key=lambda y:y[0],reverse=True):
			eds1=list(eds)
			Gdash1=Gdash.copy()
			CC1=list(CC)
			kk1=k1-1
			eds1.append((ve,chve))
			if ve in list(Gdash1.nodes):
				Gdash1.remove_node(ve)
			if chve in list(Gdash1.nodes):
				Gdash1.remove_node(chve)

			if ve in CC1:
				CC1.remove(ve)
			if chve in CC1:
				CC1.remove(chve)
			if kk1>=0 and len(list(Gdash1.edges))==0:
				theds.append(eds1)
				return
			if kk1<0:
				return
			rem_enum(eds1,Gdash1,CC1,kk1)










	
	if ve in list(Gdash.nodes):
		Gdash.remove_node(ve)
	if chve in list(Gdash.nodes):
		Gdash.remove_node(chve)

	if ve in CC:
		CC.remove(ve)
	if chve in CC:
		CC.remove(chve)
	if k1<=0 and len(list(Gdash.edges))==0:
		# print(eds)
		theds.append(eds)

	print(eds)
# for u,v in toremove:
# 	# Gdash.remove_edges_from(list(G.edges(u)))
# 	# Gdash.remove_edges_from(list(G.edges(v)))
# 	Gdash.remove_node(u)
# 	Gdash.remove_node(v)

# print(Gdash.nodes())

# print(Gdash.edges())

# for ve in CC:
# 		# k1-=1
# 	print("''''''")
# 	print(ve)
# 	print(sorted([(G.degree(x),x) for x in [n for n in G.neighbors(ve)]],key=lambda y:y[0],reverse=True))
