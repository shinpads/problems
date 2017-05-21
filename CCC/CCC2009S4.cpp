/*
 * CCC2009S4.cpp
 *
 *  Created on: May 21, 2017
 *      Author: Rob
 */

#include<iostream>
#include<list>
#include<algorithm>
#define pb push_back
const int INF = 1e9;
using namespace std;


int con[5001][5001];
int dist[5001];
bool v[5001] = {0};

int main(){
	int n,t,k,d;
	scanf("%d%d",&n,&t);
	int a,b,w;
	for(int i = 0; i<=5000; i++){
		for(int ii = 0; ii<=5000; ii++){
			con[i][ii] = -1;
		}
	}
	for(int i = 0; i<t ; i++){
		scanf("%d%d%d",&a,&b,&w);
		if(con[a][b] == -1){
			con[a][b] = w;
			con[b][a] = w;
		}
		else{
			con[a][b] = min(con[a][b],w);
			con[b][a] = min(con[b][a],w);
		}
	}
	for(int i = 0; i<=5000; i++){
		dist[i] = INF;
	}
	scanf("%d",&k);
	for(int i = 0; i<k; i++){
		scanf("%d%d",&a,&w);
		dist[a] = w;
	}
	scanf("%d",&d);

	//Dijkstra's Algorithm
	for(int i = 0; i<n; i++){
		int mindex = -1;
		for(int j = 0; j<=n; j++){
			if(!v[j] && (mindex == -1 || dist[j] < dist[mindex])){
				mindex = j;
			}
		}

		v[mindex] = true;
		if(mindex == d){break;}
		for(int i = 1; i<=5000; i++){
			if(con[mindex][i] == -1){continue;}
			else{dist[i] = min(dist[mindex]+con[mindex][i],dist[i]);}
		}
	}
	printf("%d",dist[d]);
	return 0;
}
