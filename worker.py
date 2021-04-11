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
		# print(C1)
		# print(p1)
		fourCycles(gr,C1,U1,U2,p1)
		tailIdentifier(gr,C1,U1,U2,p1)
		# tailBrancher() has been called in above func
		# recc()
	elif p1<0:
		print(p1)
		print("--------------")
	else:
		print(C1)
		print(U1)
		# print(U2)
		enumerator(gr,C1,U1)
		print("YES")
	# if p1<0:
	# 	return false
	# else check for 2-path thing

def enumerator(GG,CC,UU):
	eds=[]
	s=G.subgraph(CC)
	for l in UU:
		sd=G.subgraph(l)
		if len(list(sd.edges))!=0:
			eds.append(list(sd.edges)[0])
		else:
			un_v=l[0]
			nei_set=set(list(nx.all_neighbors(G,un_v)))
			sd.edges()
			c_set=[x for x in list(s.nodes) if len(s.edges(x))==0]
			if len(nei_set.intersection(c_set))>0:
				eds.append((un_v,list(nei_set.intersection(c_set))[0]))
			else:
				eds.append((un_v,list(nx.all_neighbors(G,un_v))[0]))
	eds.extend(list(s.edges))
	for ve in CC:
		if len([item for item in eds if item[0]==ve or item[1]==ve])==0:
			eds.append((ve,list(nx.all_neighbors(G,ve))[0]))
		if len(eds)>=k:
			break
	print(eds)


def cliqueChecker(gr,C1,U1,U2,p1):
	if(gr==G and not(nx.is_connected(gr))):
		print("en")
		return
	for c in list(nx.connected_components(gr)):
		h=gr.subgraph(c)
		n=len(list(h.nodes))
		if h.size()==n*(n-1)/2:
			# we have a clique component; move it to U1 and create new state and recc
			# print("Yes")
			newgr=gr.copy()
			U11=list(U1)
			U22=list(U2)
			U11.append(list(h.nodes))
			U22=[x for x in U2 if x in list(h.nodes)]
			newgr.remove_nodes_from(list(h.nodes))
			recc(newgr,C1,U11,U22,p1-n+1)


# now checking for 4-cycles
def fourCycles(gr,C1,U1,U2,p1):
	for l in list(nx.cycle_basis(gr)):
		if len(l)==4:
			# we have a 4cycle; we have to branch with ab,cd or bc,ad
			s=gr.subgraph(l)
			newgr=gr.copy()
			C11=list(C1)
			U11=list(U1)
			newgr.remove_nodes_from(l)
			C11.extend([s.edges[0],s.edges[2]])
			U22=list(U2)
			U22=[x for x in U2 if x in list(s.nodes)]
			recc(newgr,C11,U11,U22,p1-2)
			# now have to add the other edge set




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







