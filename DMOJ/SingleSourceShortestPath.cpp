/*
 * SingleSourceShortestPath.cpp
 *
 *  Created on: May 19, 2017
 *      Author: Rob
 */
#include<iostream>
#include<list>
using namespace std;
class Edge{
public:
	int dest, cost;
	Edge(int d, int c){
		dest = d;
		cost = c;
	}
};


list<Edge> adj[1002];
int v [1002];
int dist [1002];
int main(){
	int n,m;
	scanf("%i%i",&n,&m);
	for(int i =1; i<=n; i++){
		dist[i] = -1;
	}
	dist[1] = 0;
	for(int i = 0; i<m; i++){
		int a,b,w;
		scanf("%i%i%i",&a,&b,&w);

		adj[a].push_back(Edge(b,w));
		adj[b].push_back(Edge(a,w));
	}
	list<int> q;
	q.push_back(1);
	while(!q.empty()){
		int cur = q.front();
		q.pop_front();
		for(Edge e : adj[cur]){
			if(dist[cur] + e.cost < dist[e.dest] || dist[e.dest] == -1){
				dist[e.dest] = dist[cur] + e.cost;
				q.push_back(e.dest);
			}
		}
	}
	for(int x=1; x<=n; x++){
		printf("%i\n",dist[x]);
	}
	return 0;
}



