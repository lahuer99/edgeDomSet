# networkx is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and function of complex networks(like graphs!).
import networkx as nx

#to get the powerset 
from itertools import chain, combinations

# input graph in question
G=nx.Graph()

#parameter[if there is a k-eds?] 
k=2

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
G.add_edge(4,2);
G.add_edge(4,5);
G.add_edge(5,6);

vertices=list(G.nodes)
edges=list(G.edges)

# to store min_VCs got and give back min-eds
# let it init be set of edges of graph, if one lesser than that is got,we update eds
eds=edges

# print(sorted(G.degree,key=lambda x:x[1],reverse=True)[0])

# check starting branching with each vertex recursively
C=I=U1=[]
U2=vertices

# take node with max degree
ve=sorted(G.degree,key=lambda x:x[1],reverse=True)[0][0]

# making it recursive
def recc(gr,C1,U1,U2,p1):
	if p1>=0 and len(U2)!=0:
		if isU2done(gr,C1,U1,U2,p1):
			print("return true")
			print(C1)
			print(U1)
			# print(U2)
			print("callon2paths")
			callOn2paths(gr,C1,U1,U2,p1)
		else:
			print("''''")
			print(p1)
			print(C1)
			print(U1)
			print(U2)
			print("''''")
			cliqueChecker(gr,C1,U1,U2,p1)
			fourCycles(gr,C1,U1,U2,p1)
			tailIdentifier(gr,C1,U1,U2,p1)
	elif p1<0:
		print(p1)
		print("----/////////////////////////////////----")
	else:
		# print(C1)
		# print(U1)
		# print(U2)
		print("YES")
		theenumerator(gr,C1,U1)
		print("---------------")
		
# now have to remove that vertex,its edges and its neighbors from untracked_ and lookinto
def cleanup(untracked_vertices,untracked_edges,lookinto,v1,v2):
	nei_v1=list(nx.all_neighbors(G,v1))
	edges_v1=list(G.edges(v1))

	nei_v2=list(nx.all_neighbors(G,v2))
	edges_v2=list(G.edges(v2))

	new_untrv=[x for x in untracked_vertices if x not in nei_v1 and x not in nei_v2]
	new_untre=[(w1,w2) for w1,w2 in untracked_edges if (w1,w2) not in edges_v1 and (w1,w2) not in edges_v2]
	new_lo=[x for x in lookinto if x not in nei_v1 and x not in nei_v2]
	return new_untrv,new_untre,new_lo


def theenumerator(GG,CC,UU):
	# keep track of untouched vertices n edges
	print("enum")
	print(CC)
	print(UU)
	untracked_edges=list(edges)
	untracked_vertices=list(vertices)

	lookinto=[]
	edslite=[]
	# init make best out of vc
	# need to be by degree?
	for v1,v2 in edges:
		if v1 in CC and v2 in CC:
			edslite.append((v1,v2))
			untracked_vertices,untracked_edges,lookinto=cleanup(untracked_vertices,untracked_edges,lookinto,v1,v2)

		if len(untracked_edges)==0:
			print(edslite)
			break

	if len(CC)!=0:
		lookinto.extend(CC)

	# from U1, if any 2size clique(edge!) exists and is not covered,then add
	for l in UU:
		if len(l)==2:
			if (l[0],l[1]) in untracked_edges or (l[1],l[0]) in untracked_edges:
				edslite.append((l[0],l[1]))
				untracked_vertices,untracked_edges,lookinto=cleanup(untracked_vertices,untracked_edges,lookinto,l[0],l[1])
		elif len(l)==1 and l[0] in untracked_vertices:
			lookinto.append(l[0])

		# else if we have a clique of >2 size,we can check if any of its nodes have an edge with any node in lookinto or untracked_vertices

		if len(untracked_edges)==0:
			break
	print(untracked_edges)
	print(edslite)


def isU2done(gr,C1,U1,U2,p1):
	# print("getin")
	# print(U2)
	u2graph=gr.subgraph(U2)
	return all(len(list(x))==3 for x in list(nx.connected_components(u2graph)))
	# for l in list(nx.connected_components(u2graph)):
	# 	if len(l)!=3:
	# 		return -1
	# if len(list(nx.connected_components(u2graph)))>min(p1,k):
	# 	return 0
	# print(list(nx.connected_components(u2graph)))
	# return 1


def powerset(iterable,z):
	s=list(iterable)
	return chain.from_iterable(combinations(s,r) for r in range(1,z+1))

def callOn2paths(gr,C1,U1,U2,p1):
	print("2path mode")
	u2graph=G.subgraph(U2)
	P=list(nx.connected_components(u2graph))
	y=len(P)
	z=min(p1-y,k-y)
	Psubs=list(powerset(P,z))
	for subs in Psubs:
		# for each v0v1v2, move (v1v2 to C and v1 to U1)
		print(subs)
		for path2 in subs:
			C11=list(C1)
			U11=list(U1)
			path2=list(path2)
			if u2graph.degree(path2[0])==2:
				C11.extend([path2[1],path2[2]])
				U11.append([path2[0]])
			elif u2graph.degree(path2[1])==2:
				C11.extend([path2[0],path2[2]])
				U11.append([path2[1]])
			else:
				C11.extend([path2[0],path2[1]])
				U11.append([path2[2]])
			# U22=list(U2)
			U22=[x for x in U2 if x in C11]
			p11=p1-2
			U2new=gr.subgraph(U22)
			recc(U2new,C11,U11,U22,p11)
		# move each in P-P', move v1 to C and (v0v2) to U1 
		for path2 in [x for x in Psubs if x!=subs]:
			C11=list(C1)
			U11=list(U1)
			path2=list(path2)
			if u2graph.degree(path2[0])==2:
				U11.append([path2[1]])
				U11.append([path2[2]])
				C11.append(path2[0])
			elif u2graph.degree(path2[1])==2:
				U11.append([path2[0]])
				U11.append([path2[2]])
				C11.append(path2[1])
			else:
				U11.append([path2[0]])
				U11.append([path2[1]])
				C11.append(path2[2])
			U22=list(U2)
			U22=[x for x in U2 if x in C11]
			p11=p1-2
			U2new=gr.subgraph(U22)
			recc(U2new,C11,U11,U22,p11)			







def cliqueChecker(gr,C1,U1,U2,p1):
	print(U2)
	if(gr==G and not(nx.is_connected(gr))):
		m=len(list(h.nodes))
		if gr.size()!=m*(m-1)/2:
			return
	for c in list(nx.connected_components(gr)):
		h=gr.subgraph(c)
		n=len(list(h.nodes))
		if h.size()==n*(n-1)/2 or n==1:
			print("clique")
			print(list(h.nodes()))
			# we have a clique component; move it to U1 and create new state and recc

			# print("Yes")
			newgr=gr.copy()
			U11=list(U1)
			# U22=list(U2)
			U11.append(list(h.nodes))
			# U22=[x for x in U2 if x in list(h.nodes)]
			newgr.remove_nodes_from(list(h.nodes))
			U22=list(newgr.nodes)
			print("''''")
			print(p1)
			print(C1)
			print(U1)
			print(U2)
			print("''''")
			recc(newgr,C1,U11,U22,p1-n+1)


# now checking for 4-cycles
def fourCycles(gr,C1,U1,U2,p1):
	for l in list(nx.cycle_basis(gr)):
		if len(l)==4:
			print("4cycle")
			# we have a 4cycle; we have to branch with ab,cd or bc,ad
			s=gr.subgraph(l)
			sn=list(s.nodes)

			C11=list(C1)
			C12=list(C1)

			if sn[0] in list(nx.all_neighbors(s,sn[1])):
				if sn[0] in list(nx.all_neighbors(s,sn[2])):
					C11.extend([sn[0],sn[3]])
					C12.extend([sn[1],sn[2]])
				else:
					C11.extend([sn[0],sn[2]])
					C12.extend([sn[1],sn[3]])
			else:
				C11.extend([sn[0],sn[1]])
				C12.extend([sn[2],sn[3]])

			newgr=gr.copy()
			U11=list(U1)
			newgr.remove_nodes_from(l)
			U22=list(newgr.nodes)
			recc(newgr,C11,U11,U22,p1-2)

			# now have to add the other edge set
			newgr1=gr.copy()
			U12=list(U1)
			newgr1.remove_nodes_from(l)
			U222=list(newgr1.nodes)
			recc(newgr1,C12,U12,U222,p1-2)			




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
		print(ver)
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
	p1d=p1-1
	C1d.append(vat)
	U12=list(U1)
	newG=gr.copy()
	newG.remove_node(vat)
	U21=list(newG.nodes)
	print(U21)
	recc(newG,C1d,U12,U21,p1d)

	# ToDo branch of neighbors of vat
	C2d=list(C1)
	p2d=p1-2
	C2d.extend(list(nx.all_neighbors(gr,vat)))
	U12=list(U1)
	newG1=gr.copy()
	newG1.remove_nodes_from(list(nx.all_neighbors(gr,vat)))
	U22=list(newG1.nodes)
	recc(newG1,C2d,U12,U22,p2d)



# for (ve,de) in sorted(G.degree,key=lambda x:x[1],reverse=True):
print(ve)
# branch incl ve
C1=list(C)
# p1=p
C1.append(ve)
p1=p-1
U21=G.copy()
U21.remove_nodes_from(C1)
U212=list(U21.nodes)
print("''''")
print(p1)
print(C1)
print(U1)
print(U212)
print("''''")
recc(U21,C1,U1,U212,p1)

print("////////////////////////////////")

# branch without ve
C2=list(C)
C2.extend(list(G.neighbors(ve)))
p2=p-len(list(G.neighbors(ve)))
U22=G.copy()
U22.remove_nodes_from(C2)
U222=list(U22.nodes)
recc(U22,C2,U1,U22,p2)







