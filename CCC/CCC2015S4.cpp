/*
 * CCC2015S4.cpp
 *
 *  Created on: May 23, 2017
 *      Author: Rob
 */

#include<iostream>
#include<list>
#include<algorithm>
using namespace std;
#define pb push_back

struct Edge{
	int dest;
	int time;
	int wear;
	Edge(int d, int t, int w){
		dest = d;
		time = t;
		wear = w;
	}
};

list<Edge> cons[2001];
int k,n,m,a,b,t,w,A,B;
int dist[2001][201];
bool v[2001] = {0};
int main(){
	scanf("%d %d %d",&k,&n,&m);
	for(int i = 0; i<m; i++){
		scanf("%d%d%d%d",&a,&b,&t,&w);
		cons[a].pb(Edge{b,t,w});
		cons[b].pb(Edge{a,t,w});
	}
	scanf("%d%d",&A,&B);
	for(int i = 0; i<= 2000; i++){
		for(int ii =0; ii<=200; ii++){
			dist[i][ii] = 99999999;
		}
	}
	dist[A][0] = 0;
	//find best path
	list<int> q;
	q.pb(A);
	while(!q.empty()){
		int cur= q.front(); q.pop_front();
		v[cur] = false;
		for(Edge e : cons[cur]){
			for(int ii = 0; ii + e.wear < k; ii++){
				if(dist[cur][ii] + e.time < dist[e.dest][ii+e.wear]){
					dist[e.dest][ii+e.wear] = dist[cur][ii] + e.time;
					if(!v[e.dest]){
						v[e.dest] = true;
						q.pb(e.dest);
					}
				}
			}
		}

	}
	int ans = -1;
	for(int i = 0; i< k; i++){
		if(dist[B][i] != -1 ){
			ans = min(ans,dist[B][i]);
		}
		if(ans == -1 && dist[B][i] !=99999999 ){
		  ans = dist[B][i];
		}
	}
	printf("%d",ans);
	return 0;
}



