/*
 * VMWC2016G5.cpp
 *
 *  Created on: May 27, 2017
 *      Author: Rob
 */
/*
 * find the farthest point away from the farther point away from any point on the graph
 * O(N)
 */
#include<iostream>
#include<list>
#define pb push_back
using namespace std;
list<int> con[10001];
int n,a,b;
//find eccentricity
pair<int,int> eccen(int x){
	int dist[10001];
	fill_n(dist,10001,-1);
	dist[x] = 0;
	list<int> q;
	q.pb(x);
	int ansi = 0;
	int ansv = 0;
	while(!q.empty()){
		int cur = q.front(); q.pop_front();
		for(int c : con[cur]){
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
	scanf("%d",&n);
	for(int i = 0; i<n-1; i++){
		scanf("%d%d",&a,&b);
		con[a].pb(b);
		con[b].pb(a);
	}
	printf("%d",eccen(eccen(1).first).second);
	return 0;
}



