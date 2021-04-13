import networkx as nx

# will use modules

# to perform kernelization on input instance <G,k> and return the new instance set <G',k'>

# a linear-time kernel
# | V(G')|<= 2k'^2+2k'
# | E(G')|= O(k'^3)
# k'<= k

# input graph in question
G=nx.Graph()

#parameter[if there is a k-eds?] 
k=2

# adding vertices of graph
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)
G.add_node(9)

# adding edges of graph
G.add_edge(0,1)
G.add_edge(0,8)
G.add_edge(7,6)
G.add_edge(7,8)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,2)
G.add_edge(4,5)
G.add_edge(5,6)
G.add_edge(8,9)

vertices=list(G.nodes)
edges=list(G.edges)

G1=G.copy()

# init find a max. matching in linear time
# max. matching is a 2-factor eds[computes in O(|E|)]
M=list(nx.maximal_matching(G))

if len(M)<k+1:
	print(M)
else:
	vertices_M=[x for y in M for x in y]
	# v1 = v - vm; will be an independent set
	v1=[v for v in vertices if v not in vertices_M]
	set_v1=set(v1)

	# set of all vertices with a neighbor of deg.1
	v_nei1=[v for v in vertices_M if any(G.degree(ve)==1 for ve in list(nx.all_neighbors(G,v)))]

	# now create set of overloaded vertices
	overloaded_v=[]
	for v in vertices_M:
		nei_v=set(list(nx.all_neighbors(G,v)))
		x=len(nei_v.intersection(set_v1))
		if x+len(M)>2*k:
			overloaded_v.append(v)

	A1=list(set(overloaded_v).union(set(v_nei1)))
	print(A1)
	to_del=[]
	for v in v1:
		if all(x in A1 for x in nx.all_neighbors(G,x)):
			to_del.append(u)

	# print(to_del)
	G1.remove_nodes_from(to_del)
	print(list(G1.nodes))

	v_toadd=[]
	ed_toadd=[]
	for v in A1:
		w=[x for x in nx.all_neighbors(G,v) if x in v1]
		if len(w)!=0:
			v_toadd.append(w[0])
			ed_toadd.append((v,w[0]))

	G2=nx.Graph()
	for v in v_toadd:
		G2.add_node(v)
	for ed in ed_toadd:
		G2.add_edge(*ed)

	# Gf is final graph after kernelization
	Gf=nx.compose(G1,G2)

	print(list(Gf.nodes()))

	# overloaded_v will be the subset of eds
	# from lemma => all overloaded vertices must be in vertex set of eds
		# so we annotate these vertices [overloaded_v]
		# we also annotate all vertices who have a neighbour of deg.1 [v_nei1]


