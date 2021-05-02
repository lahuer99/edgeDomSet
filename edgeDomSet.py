# networkx is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and function of complex networks(like graphs!).
import networkx as nx

# to get graph image(stored in same dir)
import matplotlib.pyplot as plt

#to get the powerset 
from itertools import chain, combinations

# kernelization module(kernelization.py)
import kernelization

theds=[]

# making it recursive
def recc(gr,C1,I1,U1,U2,p1):
	if p1>=0 and len(U2)!=0:
		if isU2done(gr,C1,I1,U1,U2,p1):
			callOn2paths(gr,C1,I1,U1,U2,p1)
		else:
			cliqueChecker(gr,C1,I1,U1,U2,p1)
			fourCycles(gr,C1,I1,U1,U2,p1)
			tailIdentifier(gr,C1,I1,U1,U2,p1)
			vertexPicker(gr,C1,I1,U1,U2,p1)
			
	elif p1<0:
		p1=p1
	else:
		if len(theds)!=0 and len(min(theds,key=len))<=k:
			print("YES")
			print(min(theds,key=len))

			eddss=min(theds,key=len)
			pos = nx.spring_layout(G)
			values=['r' if tu in eddss or tu[::-1] in eddss else '#000000' for tu in edges ]
			weights=[5 if tu in eddss or tu[::-1] in eddss else 1 for tu in edges ]
			nx.draw(G,pos,edge_color=values,width=weights,with_labels=True)
			plt.savefig("./edsgraph.jpg")

			exit()

		# ToDo
		# for a NO instance, program runs for a long-time(have to figure out why)
		# for now, if we get past 1000 vc, we assume it to be a NO instance
		if len(theds)!=0 and len(theds)>=1000:
			print("NO")
			exit()
		theenumerator(gr,C1,I1,U1)

	
def vertexPicker(gr,C1,I1,U1,U2,p1):
	vl=[x[0] for x in sorted(gr.degree,key=lambda x:x[1],reverse=True) if x[1]>=3]
	if len(vl)==0:
		return 

	ve=vl[0]
	
	C11=list(C1)
	C11.append(ve)
	p11=p1-1
	U21=gr.copy()
	U21.remove_nodes_from(C11)
	U212=list(U21.nodes)
	recc(U21,C11,I1,U1,U212,p11)

	
	C2=list(C1)
	C2.extend(list(gr.neighbors(ve)))
	I11=list(I1)
	I11.append(ve)
	p2=p1-len(list(gr.neighbors(ve)))
	U22=gr.copy()
	U22.remove_nodes_from(C2)
	U22.remove_node(ve)
	U222=list(U22.nodes)
	recc(U22,C2,I11,U1,U222,p2)



def theenumerator(GG,CC,II,UU):
	notlook=set()
	if len(CC)==0:
		return

	Gdash=G.copy()
	k1=k
	eds=[]

	Gcopy=G.copy()
	Gcopy.remove_nodes_from([i for i in vertices if i not in CC or i in II])

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

		notlook.add(u)
		notlook.add(v)

		k1-=1
		eds.append((u,v))
		if k1>=0 and len(list(Gdash.edges))==0:
			theds.append(eds)
			return	

	if k1-len(list(Gdash.edges))>=0:
		eds.extend(list(Gdash.edges))
		theds.append(eds)
		return

	deg1=set()
	for v in list(Gdash.nodes):
		if Gdash.degree(v)<1:
			deg1.add(v)
	
	Gdash.remove_nodes_from(deg1)

	for ve in CC:
		if ve in notlook:
			continue
		chve=sorted([(G.degree(x),x) for x in [n for n in G.neighbors(ve)]],key=lambda y:y[0],reverse=True)[0][1]
		for i in sorted([(G.degree(x),x) for x in [n for n in G.neighbors(ve)]],key=lambda y:y[0],reverse=True):
			if i[1] in list(Gdash.nodes):
				if i[1] not in notlook:
					chve=i[1]
					break
				elif G.degree(chve)<=G.degree(i[1]):
					chve=i[1]


		k1-=1
		if (ve,chve) in edges:
			eds.append((ve,chve))
		else:
			eds.append((chve,ve))

		if ve in list(Gdash.nodes):
			Gdash.remove_node(ve)
		if chve in list(Gdash.nodes):
			Gdash.remove_node(chve)

		notlook.add(ve)
		notlook.add(chve)

		if ve in CC:
			CC.remove(ve)
		if chve in CC:
			CC.remove(chve)

		if len(list(Gdash.edges))==0:
			theds.append(eds)
			return	

	for i in notlook:
		if i in CC:
			CC.remove(i)

	deg1=set()
	for v in list(Gdash.nodes):
		if Gdash.degree(v)<1:
			deg1.add(v)
	
	Gdash.remove_nodes_from(deg1)

	for ve in list(Gdash.nodes):
		if ve in notlook:
			continue

		chve=sorted([(G.degree(x),x) for x in [n for n in G.neighbors(ve)]],key=lambda y:y[0],reverse=True)[0][1]
		for i in sorted([(G.degree(x),x) for x in [n for n in G.neighbors(ve)]],key=lambda y:y[0],reverse=True):
			if i[1] in list(Gdash.nodes):
				if i[1] not in notlook:
					chve=i[1]
					break
				elif G.degree(chve)<=G.degree(i[1]):
					chve=i[1]

		if (ve,chve) in eds or (chve,ve) in eds:
			continue

		if (ve,chve) in edges:
			eds.append((ve,chve))
		else:
			eds.append((chve,ve))
		k1-=1

		if ve in list(Gdash.nodes):
			Gdash.remove_node(ve)
		if chve in list(Gdash.nodes):
			Gdash.remove_node(chve)

		notlook.add(ve)
		notlook.add(chve)

		if ve in CC:
			CC.remove(ve)
		if chve in CC:
			CC.remove(chve)

		if len(list(Gdash.edges))==0:
			theds.append(eds)
			return	



def isU2done(gr,C1,I1,U1,U2,p1):
	u2graph=gr.copy()
	#old u2graphh=gr.subgraph(U2)
	return all(len(list(x))==3 for x in list(nx.connected_components(u2graph)))

def powerset(iterable,z):
	s=list(iterable)
	return chain.from_iterable(combinations(s,r) for r in range(0,z+1))

def callOn2paths(gr,C1,I1,U1,U2,p1):
	u2graph=gr.copy()
	#old u2graphh=gr.subgraph(U2)
	P=list(nx.connected_components(u2graph))
	y=len(P)
	if y>min(p1,k):
		# print("mm")
		return
	z=min(p1-y,k-y)
	Psubs=list(powerset(P,z))

	for subs in Psubs:
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

			U22=list(U2)
			U22.remove(path2[0])
			U22.remove(path2[1])
			U22.remove(path2[2])
			p11=p1-2
			U2new=gr.subgraph(U22)
			recc(U2new,C11,I1,U11,U22,p11)
		
		# move each in P-P', move v1 to C and (v0v2) to U1 
		#old for path2 in [x for x in Psubs if x!=subs]:
		# newbegin
		for path2 in [x for x in P if x not in subs]:
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
			U22.remove(path2[0])
			U22.remove(path2[1])
			U22.remove(path2[2])
			p11=p1-2
			U2new=gr.subgraph(U22)
			recc(U2new,C11,I1,U11,U22,p11)			




def cliqueChecker(gr,C1,I1,U1,U2,p1):
	for c in list(nx.connected_components(gr)):
		h=gr.subgraph(c)
		n=len(list(h.nodes))
		if h.size()==n*(n-1)/2 or n==1:
			# we have a clique component; move it to U1 and create new state and recc
			newgr=gr.copy()
			U11=list(U1)
			U11.append(list(h.nodes))
			newgr.remove_nodes_from(list(h.nodes))
			U22=list(newgr.nodes)
			recc(newgr,C1,I1,U11,U22,p1-n+1)


# now checking for 4-cycles
def fourCycles(gr,C1,I1,U1,U2,p1):
	try:
		# for l in list(nx.find_cycle(gr)):
		for l in list(nx.cycle_basis(gr)):
			if len(l)==4:
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
				# old was to remove from l
				newgr.remove_nodes_from(C11)
				U22=list(newgr.nodes)
				recc(newgr,C11,I1,U11,U22,p1-2)

				# now have to add the other edge set
				newgr1=gr.copy()
				U12=list(U1)
				newgr1.remove_nodes_from(C12)
				U222=list(newgr1.nodes)
				recc(newgr1,C12,I1,U12,U222,p1-2)			
	except:
		return



def tailIdentifier(gr,C1,I1,U1,U2,p1):
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
		tailBrancher(gr,C1,I1,U1,U2,p1,nbrs,ver)



def tailBrancher(gr,C1,I1,U1,U2,p1,nbrs,v):
	others=[]
	if(gr.degree(nbrs[v][0])==1):
		vat=nbrs[v][1]
		others=[v,nbrs[v][0]]
	else:
		vat=nbrs[v][0]
		others=[v,nbrs[v][1]]

	# vat is the deg2 vertex on which we have to further branch:2 cases - either incl vat or n(vat)
	# so we modify current graph and call recc on that
	C1d=list(C1)
	p1d=p1-2
	C1d.append(vat)
	U12=list(U1)
	U12.append(others)
	newG=gr.copy()
	newG.remove_nodes_from([v,nbrs[v][0],nbrs[v][1]])
	U21=list(newG.nodes)
	recc(newG,C1d,I1,U12,U21,p1d)

	# branch of neighbors of vat
	C2d=list(C1)
	p2d=p1-len(list(nx.all_neighbors(gr,vat)))
	C2d.extend(list(nx.all_neighbors(gr,vat)))

	U12=list(U1)
	# vat and deg1 vertex become deg0 vertices; vat is added to I, deg0 vertex can be added to U1
	if(gr.degree(nbrs[v][0])==1):
		U12.append([nbrs[v][0]])
	else:
		U12.append([nbrs[v][1]])
	I11=list(I1)
	I11.append(vat)

	newG1=gr.copy()
	newG1.remove_nodes_from(list(nx.all_neighbors(gr,vat)))
	newG1.remove_nodes_from([v,nbrs[v][0],nbrs[v][1]])
	U22=list(newG1.nodes)
	recc(newG1,C2d,I11,U12,U22,p2d)


# kernel() in module returns kernel graph; if it is empty, kernelization algo. has already given YES output
G=kernelization.kernel()

# parameter[if there is a k-eds?] (imported from kernelization module)
k=kernelization.k

# ToDo
# annotated set(must be in V(eds))
# can be set as A1 union CC
A1=kernelization.A1

# max size possible for vc [p<0 => NO instance]
p=2*k

vertices=list(G.nodes)
edges=list(G.edges)

# the state tuple 
C=I=U1=[]
U2=vertices


if len(vertices)==0:
	exit()
else:
	pos = nx.spring_layout(G)
	nx.draw(G,pos,with_labels=True)
	plt.savefig("./graph.jpg")
	plt.clf()

	recc(G,C,I,U1,U2,p)

	if len(theds)==0 or len(min(theds,key=len))>k:
		print("NO")
	else:
		print("YES")
		print(min(theds,key=len))
		eddss=min(theds,key=len)
		pos = nx.spring_layout(G)
		values=['r' if tu in eddss or tu[::-1] in eddss else '#000000' for tu in edges ]
		weights=[5 if tu in eddss or tu[::-1] in eddss else 1 for tu in edges ]
		nx.draw(G,pos,edge_color=values,width=weights,with_labels=True)
		plt.savefig("./edsgraph.jpg")