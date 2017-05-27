/*
 * HidenSeek.cpp
 *
 *  Created on: May 27, 2017
 *      Author: Rob
 */
/*
 * start by storing all values in a 2d-array.
 * keep track of where you start and where all of the hiders are.
 * for the start position and all the hider's positions, find the shortest distances (using BFS) to
 * all other hiders.
 * because t <= 5, we can easily go over all permutations of paths through all hiders in factorial time.
 * go through all paths and keep track of which has smallest distance and print out answer
 *
 * O(T! + TNM)
 */
#include<iostream>
#include<list>
#include<vector>
#include<algorithm>
#define pb push_back
#define mp point
using namespace std;
char vals[21][21];
int dist[21][21][21][21];

struct point{
	int x;
	int y;
};
point moves[] = {mp{1,0},mp{-1,0},mp{0,1},mp{0,-1}};
vector<point> hiders;
point start;
int n,m,t;
char p;
void BFS(point s){
	list<point> q;
	q.pb(s);
	dist[s.x][s.y][s.x][s.y] = 0;
	int cx,cy;
	while(!q.empty()){
		cx = q.front().x;
		cy = q.front().y;
		//printf("%d %d \n",cx,cy);
		q.pop_front();
		for(point t : moves){
			if(cx+t.x >= 0 && cx+t.x < m && cy+t.y >= 0 && cy+t.y < n){
				if(dist[s.x][s.y][cx+t.x][cy+t.y] == -1 && vals[cx+t.x][cy+t.y] != 'X'){
					dist[s.x][s.y][cx+t.x][cy+t.y] = dist[s.x][s.y][cx][cy] + 1;
					q.pb(point{cx+t.x,cy+t.y});
				}
			}
		}
	}
}

int main(){
	for(int a = 0; a<=20; a++){
		for(int b = 0; b<= 20; b++){
			for(int c = 0; c<=20; c++){
				for(int d = 0; d<=20; d++){
					dist[a][b][c][d] = -1;
				}
			}
		}
	}
	//create map
	scanf("%d%d%d",&n,&m,&t);
	for(int y = 0; y<n; y++){
		for(int x = -1; x<m; x++){
			scanf("%c",&p);
			if(x>= 0){
				vals[x][y] = p;
			}
			if(p == 'H'){
				hiders.pb(point{x,y});
			}
			if(p == 'G'){
				start = point{x,y};
			}
		}
	}
	BFS(start);
	for(point h : hiders){
		BFS(h);
	}
	int ans = 999999;
	int cans = 0;
	vector<int> perm;
	for(int i = 0; i<t; i++){
	  perm.pb(i);
	}
	do{
		cans = dist[start.x][start.y][hiders[perm[0]].x][hiders[perm[0]].y];
		for(int i = 0; i<t-1; i++){
			cans += dist[hiders[perm[i]].x][hiders[perm[i]].y][hiders[perm[i+1]].x][hiders[perm[i+1]].y];
		}
		ans = min(ans,cans);
	}while(next_permutation(perm.begin(),perm.end()));
	printf("%d",ans);





	return 0;
}



