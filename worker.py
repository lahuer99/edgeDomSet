# networkx is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and function of complex networks(like graphs!).
import networkx as nx

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
G.add_edge(7,6);
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

# take node with max degree
ve=sorted(G.degree,key=lambda x:x[1],reverse=True)[0][0]
# print(v)
# now we have 2 branches - one incl v in C and other incl neighbours of v in C
# print(v)


# making it recursive
def recc(gr,C1,U1,U2,p1):
	if p1>=0 and len(U2)!=0:
		cliqueChecker(gr,C1,U1,U2,p1)
		print(C1)
		print(p1)
		tailIdentifier(gr,C1,U1,U2,p1)
		# tailBrancher() has been called in above func
		# recc()
	elif p1<0:
		print(p1)
		print("--------------")
	else:
		print("YES")
	# if p1<0:
	# 	return false
	# else check for 2-path thing


def cliqueChecker(gr,C1,U1,U2,p1):
	if(gr==G and not(nx.is_connected(gr))):
		print("en")
		return
	for c in list(nx.connected_components(gr)):
		h=gr.subgraph(c)
		n=len(list(h.nodes))
		if h.size()==n*(n-1)/2:
			# we have a clique component; move it to U1 and create new state and recc
			print("Yes")
			newgr=gr.copy()
			U11=list(U1)
			U22=list(U2)
			U11.extend(list(h.nodes))
			U22=[x for x in U2 if x in list(h.nodes)]
			newgr.remove_nodes_from(list(h.nodes))
			recc(newgr,C1,U11,U22,p1-n+1)





def tailIdentifier(gr,C1,U1,U2,p1):
	# tail identifier
	# get deg2 nodes
	nbrs={}
	for v in list(gr.nodes):
		if gr.degree(v)==2:
			nbrs[v]=list(nx.all_neighbors(gr,v))

	toremove=[]
	for (k,v) in nbrs.items():
		if not (gr.degree(v[0])==1 or gr.degree(v[1])==1):
			toremove.append(k)

	for k in toremove:
		del nbrs[k]
	
	for ver in list(nbrs.keys()):
		tailBrancher(gr,C1,U1,U2,p1,nbrs,ver)



def tailBrancher(gr,C1,U1,U2,p1,nbrs,v):
	# incl vat(ie, vertex w deg>1)
	if(gr.degree(nbrs[v][0])==1):
		vat=nbrs[v][1]
	else:
		vat=nbrs[v][0]

	# vat is the deg2 vertex on which we have to further branch:2 cases - either incl vat or n(vat)
	# so we modify current graph and call recc on that
	C1d=list(C1)
	p1d=p1-2
	C1d.append(vat)
	U2=list(U2)
	U1=list(U1)
	newG=gr.copy()
	newG.remove_node(vat)
	recc(newG,C1d,U1,U2,p1d)

	# ToDo branch of neighbors of vat

	# not incl v,ie ,incl v in I and incl nbrs[v] in VC
	# V2=[]
	# V2.extend(list(nx.all_neighbors(gr,vat))) 
	# VCs.append(V2)



# for (ve,de) in sorted(G.degree,key=lambda x:x[1],reverse=True):
	# branch incl ve
C1=list(C)
p1=p
C1.append(ve)
p1=p1-1
U21=G.copy()
U21.remove_nodes_from(C1)
recc(U21,C1,U1,U2,p1)
# print("////////////////////////////////")
	# branch without ve
	# recc(G.copy,list(C)+list(G.neighbors(ve)),list(U1),list(U2),p-(len(list(G.neighbors(ve)))))








# C1=list(C)
# C2=list(C)
# p1=p
# p2=p
# C1.append(v)
# p1=p1-1
# C2.extend(list(G.neighbors(v)))
# p2=p2-len(C2)

# now have to get modified U2 corresponding to both C1 and C2
# U21=G.copy()
# # .subgraph(list(U2))
# U22=G.copy()
# # .subgraph(list(U2))

# U21.remove_nodes_from(C1)
# U22.remove_nodes_from(C2)

# print(U21.edges)
# print(U22.edges)
# print(p1)
# print(p2)

# we have to check for new clique components each time a graph is modified
# check if it is component-ed and if so, check if any of them is a clique(that will be called a clique component!?)



# check for tails
# tails_U21=tails_U22={}
# def tailIdentifier(gr,nbrs):
# 	# tail identifier
# 	# get deg2 nodes
# 	for v in list(gr.nodes):
# 		if gr.degree(v)==2:
# 			nbrs[v]=list(nx.all_neighbors(gr,v))

# 	toremove=[]
# 	for (k,v) in nbrs.items():
# 		if not (gr.degree(v[0])==1 or gr.degree(v[1])==1):
# 			toremove.append(k)

# 	for k in toremove:
# 		del nbrs[k]
# 	return list(nbrs.keys())
# nbrs_U21={}
# tails_U21=tailIdentifier(U21,nbrs_U21)
# nbrs_U22={}
# tails_U22=tailIdentifier(U22,nbrs_U22)

# VCs=[]
# # got tails in both graphs,now have to branch on them
# def tailBrancher(gr,nbrs,v):
# 	# incl vat(ie, vertex w deg>1)
# 	V1=[]
# 	if(gr.degree(nbrs[v][0])==1):
# 		vat=nbrs[v][1]
# 	else:
# 		vat=nbrs[v][0]
# 	V1.append(vat)
# 	VCs.append(V1)

# 	# not incl v,ie ,incl v in I and incl nbrs[v] in VC
# 	V2=[]
# 	V2.extend(list(nx.all_neighbors(gr,vat))) 
# 	VCs.append(V2)

# newU21s=[]
# for ve in tails_U21:
# 	print(ve)
# 	tailBrancher(U21,nbrs_U21,ve)

# print(C1)
# print(p1)
# print(VCs)
# until no 2-path component exists


# print(G.edges(v))