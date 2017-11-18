/*
 *  DFS starting at X until Y making sure to save where you came from
 *  then trace back and save all nodes of the path
 *  then you just gotta expand from each node on the path and calculate distance from that node to all
 *  none path nodes
 *  then go over all rabit nodes and find min
 *
 */
#include<iostream>
#include<list>
#include<string.h>
#include<algorithm>
#define pb push_back
using namespace std;
int v[200001] = {0};
list<int> con[200001];
list<int> rabs;
bool path[200001];
int dists[200001];
bool vis[200001];
int n,r,x,y,a,b;
void setdist(int xx, int vv){
	//printf("setdist(%d, %d)\n",xx,vv);
	vis[xx] = true;
	dists[xx] = vv;
	for(int pp : con[xx]){
		//printf("check to: %d, cur dist: %d, isPath: %d\n",pp,dists[pp],path[pp]);
		if(!path[pp] && !vis[pp]){
			setdist(pp,vv+1);
		}
	}

}
int main(){
	scanf("%d%d",&n,&r);
	for(int i = 0; i<n-1; i++){
		scanf("%d%d",&a,&b);
		con[a].pb(b);
		con[b].pb(a);
	}
	for(int i = 0; i<r; i++){
		scanf("%d",&a);
		rabs.pb(a);
	}
	scanf("%d %d",&x,&y);

	//find path from x to y and save where each node came from
	list<int> q;
	v[x] = x;
	q.pb(x);
	int cur;
	while(!q.empty()){
		int cur = q.front(); q.pop_front();
		for(int p : con[cur]){
			if(v[p] == 0){
				v[p] = cur;
				q.pb(p);
			}
			if(p == y){break;}
		}
	}
	//mark which nodes are part of path
	cur = y;
	path[x] = true;
	dists[x] = 0;
	while(cur != x){
		dists[cur] = 0;
		path[cur] = true;
		cur = v[cur];
	}
	cur = y;
	while(cur != x){
		setdist(cur,0);
		cur = v[cur];
	}
	setdist(x,0);
	int ans = 3000000;
	for(int p : rabs){
		ans = min(ans,dists[p]);
	}
	printf("%d\n",ans);

	return 0;
}

