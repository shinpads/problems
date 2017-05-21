/*
 * PersuitOfKnowledge.cpp
 *
 *  Created on: May 20, 2017
 *      Author: Rob
 */

#include<iostream>
#include<list>
#include<algorithm>
using namespace std;
list<int> hallways[1002];
int dist[1002][1002];
int main(){
	int m,n,t,Q;
	scanf("%i%i%i",&n,&m,&t);
	for(int i = 0; i<m; i++){
		int a,b;
		scanf("%i%i",&a,&b);
		hallways[a].push_back(b);
	}


	list<int> q;

	for(int s = 1; s<= n; s++){

		for(int i = 0; i<1002; i++){
			dist[s][i] = -1;
		}
		dist[s][s] = 0;
		q.push_back(s);

		while(!q.empty()){
			int cur = q.front();
			q.pop_front();
			for(int x : hallways[cur]){
				if(dist[s][x] == -1){
					q.push_back(x);
					dist[s][x] = dist[s][cur] +1;
				}
				dist[s][x] = min(dist[s][x],dist[s][cur]+1);
			}

		}

	}
	scanf("%i",&Q);
	for(int i = 0; i<Q; i++){
		int a,b;
		scanf("%i%i",&a,&b);
		if(dist[a][b] == -1){
			printf("Not enough hallways!\n");
		}else{
			printf("%i\n",dist[a][b]*t);
		}
	}


	return 0;
}


