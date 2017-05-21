/*
 * CCC2010J5.cpp
 *
 *  Created on: May 20, 2017
 *      Author: Rob
 */

#include<iostream>
#include<list>
using namespace std;
struct pos{
	int x;
	int y;
};
int dist[9][9];
pos moves[] = {pos{-2,1},pos{-2,-1},pos{-1,2},pos{-1,-2},pos{1,2},pos{2,1},pos{2,-1},pos{1,-2}};
int cx,cy;
int main(){
	for(int i = 0; i<=8; i++){
		for(int x = 0; x<=8; x++){
			dist[x][i] = -1;
		}
	}
	int sx,sy,ex,ey;
	scanf("%i%i%i%i",&sx,&sy,&ex,&ey);
	dist[sx][sy] = 0;
	list<pos> q;
	q.push_front(pos{sx,sy});
	while(!q.empty()){
		pos cur = q.front();

		q.pop_front();
		if(cur.x == ex && cur.y == ey){break;}
		for(pos t : moves){
			if(cur.x+t.x <9 && cur.x+t.x > 0 && cur.y+t.y > 0 && cur.y + t.y < 9){
				if(dist[t.x+cur.x][t.y+cur.y] == -1){
					dist[t.x+cur.x][t.y+cur.y] = dist[cur.x][cur.y] +1;
					q.push_back(pos{t.x+cur.x,t.y+cur.y});
				}
			}
		}

	}
	printf("%i",dist[ex][ey]);
	return 0;
}


