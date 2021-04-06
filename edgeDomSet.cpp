// Edge Dominating Set: Given a graph G=(V,E) and an integer parameter k, is there a subset E' of E of atmost k edges such that every edge not in E' is adjacent to atleast one edge in E'.

#include<iostream>
#include<list>
#include<algorithm>

using namespace std;

class Graph{
public:
	int V;
	list<int> *adj;

	Graph(int v){
		this->V=v;
		adj=new list<int>[v];
	}

	void addEdge(int v,int w){
		adj[v].push_back(w);
		adj[w].push_back(v);
	}

	void printGraph(){
		for(int i=0;i<this->V;i++){
			cout<<i<<"->";
			// adj[i].sort();
			for(auto j=adj[i].begin();j!=adj[i].end();j++){
				cout<<*j<<"->";
			}
			cout<<endl;
		}
	}

	void cliqueFinder(){
		
	}


};

//use 5 partitions of vertices G,C,I,U1,U2(init = V)

//run till U2-> 2paths

int main(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif

	Graph G(8);
	G.addEdge(0,1);
	G.addEdge(0,7);
	G.addEdge(7,6);
	G.addEdge(1,2);
	G.addEdge(2,3);
	G.addEdge(3,4);
	G.addEdge(2,4);
	G.addEdge(4,5);
	G.addEdge(5,6);

	G.printGraph();

	return 0;
}