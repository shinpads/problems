#include<iostream>
#include<list>
using namespace std;
#define pb push_back

class Road{
public:
	int dest, cost;
	Road(int a, int b){
		dest = a;
		cost = b;
	}
};


list<Road> con[100001];
int cost[100001];
int dist[100001];
int main(){
	int n,m;
	int a,b,d;

	scanf("%d%d",&n,&m);
	for(int i = 0; i<=n; i++)
		cost[i] = -1;
	
	
	for(int i = 0; i<m; i++){
		scanf("%d%d%d",&a,&b,&d);
		con[a].pb(Road(b,d));
		con[b].pb(Road(a,d));
	}
	cost[1] = 0;
	dist[1] = 0;
	list<int> q;
	q.pb(1);
	while(!q.empty()){
		int cur = q.front(); q.pop_front();
		for(Road r : con[cur]){
			if(cost[cur] + r.cost < cost[r.dest] || cost[r.dest] == -1|| (cost[cur] + r.cost == cost[r.dest] && dist[cur]+1 < dist[r.dest])){
				cost[r.dest] = cost[cur] + r.cost;
				dist[r.dest] = dist[cur] + 1;
				q.pb(r.dest);
			}
		}
	}
	if(cost[n] == -1)
	  printf("%d\n",cost[n]);
	else
	  printf("%d %d\n",cost[n],dist[n]);

	return 0;
}

