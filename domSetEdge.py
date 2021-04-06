import networkx as nx



G=nx.Graph()

k=4

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

U1=C=I=[]
U2=vertices

# getting all cliques of the graph
for cl in nx.find_cliques(G):
	if(tuple(cl) not in edges and tuple(cl)[::-1] not in edges):
		U1.append(cl)
		p=p-len(cl)+1
		for el in cl:
			U2.remove(el)


# either create an init graph of U2 and remove acc. or create each time

# currently creating a new U2 graph
U2G=nx.Graph()
for v in U2:
	U2G.add_node(v)

U2G_vertices=list(U2G.nodes)

for (u,v) in edges:
	if u in U2G_vertices and v in U2G_vertices:
		U2G.add_edge(u,v)

U2G_edges=list(U2G.edges)
# now we have new U2 graph, without any clique components


# tail identifier
# get deg2 nodes
# stores allneighbours of deg2 vertices in nbrs
nbrs={} 
for v in U2G_vertices:
	if U2G.degree(v)==2:
		nbrs[v]=list(nx.all_neighbors(U2G,v))

toremove=[]
for (k,v) in nbrs.items():
	if not (U2G.degree(v[0])==1 or U2G.degree(v[1])==1):
		toremove.append(k)

for k in toremove:
	del nbrs[k]

tails=list(nbrs.keys())
# tails is the set of tails in U2G
# now have to branch on them,ie , either incl vertices in tails or not incl them
# print(tails)


# set of vertex covers V obtained after branching
VCs=[]


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


# also have to modify new U2G s for each stage
# MAKE THIS A FUNCTION !!

# incl 7
VC1=VCs[0]

# U2_clone=U2G
U2G1=nx.Graph()
# func start
for v in U2G.nodes:
	if v not in VC1:
		U2G1.add_node(v)

U2G1_vertices=list(U2G1.nodes)

for (u,v) in edges:
	if u in U2G1_vertices and v in U2G1_vertices:
		U2G1.add_edge(u,v)

U2G1_edges=list(U2G1.edges)
# func end



# excl 7
VC2=VCs[1]
U2G2=nx.Graph()
# func start
for v in U2G.nodes:
	if v not in VC2:
		U2G2.add_node(v)

U2G2_vertices=list(U2G2.nodes)

for (u,v) in edges:
	if u in U2G2_vertices and v in U2G2_vertices:
		U2G2.add_edge(u,v)

U2G2_edges=list(U2G2.edges)
# func end

print(U1)

# print(edges)

# print(U2G1.edges)
# print(U2G2.edges)

# print(list(nx.find_cliques(U2G1)))


# tail detection and dealing


# print(U2G_vertices)
# print(U2G_edges)

# print(p)

