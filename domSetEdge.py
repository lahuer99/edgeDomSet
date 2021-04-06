# networkx is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and function of complex networks(like graphs!).
import networkx as nx

# input graph in question
G=nx.Graph()

#parameter[if there is a k-eds?] 
k=4

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
G.add_edge(7,6);
G.add_edge(1,2);
G.add_edge(2,3);
G.add_edge(3,4);
G.add_edge(2,4);
G.add_edge(4,5);
G.add_edge(5,6);

# store vertices of graph in a list
vertices=list(G.nodes)

# store edges of graph in a list
edges=list(G.edges)

# init set of deciders
U1=C=I=[]
U2=vertices

# we run he algo. till U2 is empty or till p<0 => NO
# (in the first case, U1 U C U I = vertices) and if p>=0 =>YES


# NEED TO BRING IN OOPS!! 


# getting all cliques of the graph
def cliqueRemover(Gr,pr):
	for cl in nx.find_cliques(Gr):
		print(cl)
		if(tuple(cl) not in edges and tuple(cl)[::-1] not in edges):
			U1.append(cl)
			pr=pr-len(cl)+1
			for el in cl:
				if el in U2:
					U2.remove(el)
				# else:
					# print(el)
	print("------------------")	
	return pr


# to be called after clique removal
def updatedU2_postclique():
	# currently creating a new U2 graph,without cliques
	U2G=nx.Graph()
	for v in U2:
		U2G.add_node(v)

	U2G_vertices=list(U2G.nodes)

	for (u,v) in edges:
		if u in U2G_vertices and v in U2G_vertices:
			U2G.add_edge(u,v)
	return U2G

# now we have new U2 graph, without any clique components
p=cliqueRemover(G,p)
U2G=updatedU2_postclique()
U2G_vertices=list(U2G.nodes)
U2G_edges=list(U2G.edges)

tails={}
# stores allneighbours of deg2 vertices in nbrs
nbrs={} 
def tailIdentifier():
	# tail identifier
	# get deg2 nodes
	for v in U2G_vertices:
		if U2G.degree(v)==2:
			nbrs[v]=list(nx.all_neighbors(U2G,v))

	toremove=[]
	for (k,v) in nbrs.items():
		if not (U2G.degree(v[0])==1 or U2G.degree(v[1])==1):
			toremove.append(k)

	for k in toremove:
		del nbrs[k]
	return list(nbrs.keys())

# tails is the set of tails in U2G
tails=tailIdentifier()


# set of vertex covers V obtained after branching
VCs=[]

# now have to branch on them,ie , either incl vertices in tails or not incl them
def tailBrancher(v):
	# incl vat(ie, vertex w deg>1)
	V1=[]
	if(U2G.degree(nbrs[v][0])==1):
		vat=nbrs[v][1]
	else:
		vat=nbrs[v][0]
	V1.append(vat)
	VCs.append(V1)

	# not incl v,ie ,incl v in I and incl nbrs[v] in VC
	V2=[]
	V2.extend(list(nx.all_neighbors(U2G,vat))) 
	VCs.append(V2)

# we have a list VCs, of all possible vertex cover we get from branching on diff tails
for v in tails:
	tailBrancher(v)


# NEED TO TAKE ONLY ANY ONE TO CHECK FOR YES/NO INSTANCE
# can take first set
# p reduces by 2 in both branches
p=p-2

# also have to modify new U2G s for each stage
# MAKE THIS A FUNCTION !!
def updatedU2s_postBranch(D):
	U=nx.Graph()
	for v in U2G.nodes:
		if v not in D:
			U.add_node(v)

	U_vertices=list(U.nodes)

	for (u,v) in edges:
		if u in U_vertices and v in U_vertices:
			U.add_edge(u,v)
	return U


# since here we are doing k-eds,we need to check for only 2 branches(ie, for branching of one vertex)=>2 new U2 graphs that we may get[one w addn of v, and other w addn of n[v]]
# => 2cases for p

p1=p2=p

# incl 7
VC1=VCs[0]

U2G1=updatedU2s_postBranch(VC1)
U2G1_vertices=list(U2G1.nodes())
U2G1_edges=list(U2G1.edges())

# in the first case, we get a new U2 with  2clique components
p1=cliqueRemover(U2G1,p1)
U2G11=updatedU2_postclique()
p1=p1-2

# excl 7
VC2=VCs[1]

U2G2=updatedU2s_postBranch(VC2)
U2G2_vertices=list(U2G2.nodes())
U2G2_edges=list(U2G2.edges())

# in the second case, we get back an empty U2

print(U1)

print(p1)
print(U2G1.edges)
print(VC1)

print(p2)
print(U2G2.edges)
print(VC2)





