/*
 * Oversleep.cpp
 *
 *  Created on: May 22, 2017
 *      Author: Rob
 */
#include<iostream>
#include<list>
using namespace std;
#define pb push_back
#define mp make_pair
bool found = false;
list<pair<int,int>> poss = {mp(1,0),mp(-1,0),mp(0,1),mp(0,-1)};
struct Pos{
	int x;
	int y;
};
int dist[1002][1002] = {0};
char vals[1002][1002];
int y,x;
char c;
Pos start;
Pos en;

int main(){
	scanf("%d%d",&y,&x);
	for(int i = 0; i < y; i++){
		for(int ii = -1; ii < x; ii++){
			scanf("%c",&c);
			if(c == 's'){
				start = Pos{ii,i};
			}
			if(c == 'e'){
				en = Pos{ii,i};
			}
            if(ii>-1){
			    vals[ii][i] = c;
            }

		}
	}

	list<Pos> q;
	q.pb(start);
	dist[start.x][start.y] = -1;
	while(!q.empty()){
		Pos cur = q.front(); q.pop_front();
		if(cur.x == en.x && cur.y == en.y){
			found = true;
			break;
		}
		for(pair<int,int> e : poss){

			if(cur.x + e.first < x && cur.x + e.first >= 0 && cur.y + e.second >= 0 && cur.y + e.second < y){
				if(dist[cur.x+e.first][cur.y+e.second] == 0 && vals[cur.x+e.first][cur.y+e.second] != 'X'){
				dist[cur.x+e.first][cur.y+e.second] = dist[cur.x][cur.y] +1;
				q.pb(Pos{cur.x+e.first,cur.y+e.second});
				}
			}
		}

	}
	if (!found){
		printf("-1");
	}else{
		printf("%d",dist[en.x][en.y]);
	}

	return 0;
}
