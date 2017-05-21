/*
 * CCC2016S3.cpp
 *
 *  Created on: May 21, 2017
 *      Author: Rob
 */


#define pb push_back
#include<iostream>
#include<algorithm>
#include<list>
using namespace std;
int size;
bool pho[1000002] = {0};
list<int> con[1000002];
bool leaf [1000002] = {0};
bool isleaf(int x){
	if(pho[x]){return false;}
	bool f = false;
	for(int c : con[x]){
		if(!leaf[c]){
			if(f){return false;}
			f = true;
		}
	}
	return true;
}
//return eccentricity of graph
pair<int,int> eccen(int x){
	int dist[1000002];
	fill_n(dist,1000002,-1);
	dist[x] = 1;
	list<int> q;
	q.pb(x);
	int ansi = 0;
	int ansv = 0;
	while(!q.empty()){
		int cur = q.front(); q.pop_front();
		for(int c : con[cur]){
			if(leaf[c]){continue;}
			if(dist[c] == -1){
				dist[c] = dist[cur] + 1;
				ansi = c;
				ansv = dist[c];
				q.pb(c);
			}
		}
	}

	return make_pair(ansi,ansv);

}
int main(){
	int n,m;
	scanf("%d%d",&n,&m);
	size = n;
	int x;
	for(int i = 0; i<m; i++){
		scanf("%d",&x);
		pho[x] = true;
	}
	int a,b;
	for(int i = 0; i<n-1; i++){
		scanf("%d%d",&a,&b);
		con[a].pb(b);
		con[b].pb(a);
	}

	// find out where all the leaves are at
	list<int> q;
	for(int i = 0; i<n; i++){
		if(con[i].size() == 1  && !pho[i]){
			q.pb(i);
			leaf[i] = true;
			size --;
		}
	}

	while(!q.empty()){
		int cur = q.front(); q.pop_front();
		for(int c : con[cur]){
			if(leaf[c]){continue;}
			if(isleaf(c)){
				leaf[c] = true;
				size --;
				q.pb(c);
			}
		}
	}

	int start = 0;
	for(int i = 0; i<n; i++){
		if(pho[i]){
			start = i;
			break;
		}
	}
	pair<int,int> node1 = eccen(start);
	pair<int,int> node2 = eccen(node1.first);
	int ans = ((2*size) - 1) - node2.second;
	printf("%d",ans);

	return 0;
}
