/*
 * IsItATree.cpp
 *
 *  Created on: Jun 5, 2017
 *      Author: Rob
 */

#define pb push_back
#define mp make_pair
#include<iostream>
#include<list>
using namespace std;
bool v[4] = {0};
list<int> con[4];
int cur = -1;
int main(){
	for(int y = 0; y<4; y++){
		for(int x = 0; x<4; x++){
			scanf("%d",&cur);
			if(cur == 1){ con[y].pb(x);}
		}
	}
	//BFS
	int start = 0;
	for(int i = 0; i<4; i++){
		if(!con[i].empty()){
			start = i; break;
		}
	}
	list<pair<int,int>> q;
	cur = -1;
	int last = 0;
	q.pb(mp(start,-1));
	while(!q.empty()){
		cur = q.front().first; last = q.front().second; q.pop_front();
		v[cur] = true;
		for(int c : con[cur]){
		  if(c == last){
		    continue;
		  }
			if(v[c]){
				printf("No");
				return 0;
			}
			else{
				q.pb(mp(c,cur));
			}
		}
	}
	printf("Yes");
	return 0;
}

