# networkx is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and function of complex networks(like graphs!).
import networkx as nx

# to perform kernelization on input instance <G,k> and return the new instance set <G',k'>

# a linear-time kernel
# | V(G')|<= 2k'^2+2k'
# | E(G')|= O(k'^3)
# k'<= k

# input graph in question
Gk=nx.Graph()

#parameter[if there is a k-eds?] 
k=3

# adding vertices of graph
Gk.add_node(0)
Gk.add_node(1)
Gk.add_node(2)
Gk.add_node(3)
Gk.add_node(4)
Gk.add_node(5)
Gk.add_node(6)
Gk.add_node(7)
# Gk.add_node(8)
# Gk.add_node(9)
# Gk.add_node(10)
# Gk.add_node(11)
# Gk.add_node(12)
# Gk.add_node(13)
# Gk.add_node(14)
# Gk.add_node(15)
# Gk.add_node(16)


# adding edges of graph
Gk.add_edge(0,1)
Gk.add_edge(1,2)
Gk.add_edge(2,3)
Gk.add_edge(3,4)
Gk.add_edge(4,5)
Gk.add_edge(5,6)
Gk.add_edge(6,7)
Gk.add_edge(7,0)
Gk.add_edge(2,4)

# Gk.add_edge(0,12)
# Gk.add_edge(12,13)
# Gk.add_edge(13,2)

# Gk.add_edge(6,15)

# Gk.add_edge(0,14)
# Gk.add_edge(7,14)

# Gk.add_edge(3,8)
# Gk.add_edge(8,9)
# Gk.add_edge(8,10)
# Gk.add_edge(10,11)
# Gk.add_edge(9,11)
# Gk.add_edge(9,16)



vertices=list(Gk.nodes)
edges=list(Gk.edges)

G1=Gk.copy()

# init find a max. matching in linear time
# max. matching is a 2-factor eds[computes in O(|E|)]
M=list(nx.maximal_matching(Gk))
A1=[]
def kernel():
	if len(M)<k+1:
		print("YESss")
		print(M)
		return nx.empty_graph()
	else:
		vertices_M=[x for y in M for x in y]
		# v1 = v - vm; will be an independent set
		v1=[v for v in vertices if v not in vertices_M]
		set_v1=set(v1)

		# set of all vertices with a neighbor of deg.1
		v_nei1=[v for v in vertices_M if any(Gk.degree(ve)==1 for ve in list(nx.all_neighbors(Gk,v)))]

		# now create set of overloaded vertices
		overloaded_v=[]
		for v in vertices_M:
			nei_v=set(list(nx.all_neighbors(Gk,v)))
			x=len(nei_v.intersection(set_v1))
			if x+len(M)>2*k:
				overloaded_v.append(v)

		A1=list(set(overloaded_v).union(set(v_nei1)))
		to_del=[]
		for v in v1:
			if all(x in A1 for x in nx.all_neighbors(Gk,x)):
				to_del.append(v)

		G1.remove_nodes_from(to_del)

		v_toadd=[]
		ed_toadd=[]
		for v in A1:
			w=[x for x in nx.all_neighbors(Gk,v) if x in v1]
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
		return Gf