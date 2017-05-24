#include<iostream>
#include<list>
#include<string>
#include<array>
#include<algorithm>
#define pb push_back
#define mp make_pair
using namespace std;
int r,c,sx,sy,ex,ey,t;
int bestvalue = -1;
char ch;
char vals[1001][1001];
int dist[1001][1001];

pair<int,int> moves[] = {mp(1,0),mp(-1,0),mp(0,1),mp(0,-1)};
int main(){
	scanf("%d%d%d%d%d%d",&r,&c,&sy,&sx,&ey,&ex);
	for(int i = 0; i < r; i++){
		for(int ii = -1; ii <c ; ii++){
		scanf("%c",&ch);
		if(ii >= 0){
			vals[ii][i] = ch;
		}
		}

	}

	scanf("%d",&t);
	for(int i = 0; i<t; i++){
		int tx,ty;
		scanf("%d%d",&ty,&tx);
		vals[tx][ty] = 'T';
	}

	for(int i = 0; i<= 1000; i++){
		for(int ii = 0; ii <= 1000; ii++){
			dist[i][ii] = -1;
		}
	}
	list<pair<int,int>> q;
	q.pb(mp(sx,sy));
	dist[sx][sy] = 0;
	int cx,cy;
	while(!q.empty()){
		cx = q.front().first;
		cy = q.front().second;
		if(vals[cx][cy] == 'T'){
		  if(bestvalue == -1){
		    bestvalue = dist[cx][cy];
		  }else{
			bestvalue = min(bestvalue,dist[cx][cy]);
		  }
		}
		//printf("%d %d %c %d\n",cx,cy,vals[cx][cy],dist[cx][cy]);
		q.pop_front();
		for(pair<int,int> con : moves){
			int ax = con.first; int ay = con.second;
			if(cx+ax < c && cx+ax >= 0 && cy+ay >= 0 && cy+ay < r){
				if(vals[cx+ax][cy+ay] != 'X'){
					if(dist[cx+ax][cy+ay] == -1 || dist[cx][cy] +1 < dist[cx+ax][cy+ay]){
						dist[cx+ax][cy+ay] = dist[cx][cy]+1;
						q.pb(mp(cx+ax,cy+ay));
					}

				}
			}
		}

	}
	//printf("%d %d\n",dist[ey][ex],bestvalue);
	printf("%d",max(dist[ex][ey] - bestvalue,0));
	return 0;
}
